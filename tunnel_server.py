import socket
import select
import struct
import time
import logging
import os
import psutil
import argparse

# Configure the logging module
logging.basicConfig(filename='tunnel_server.log', level=logging.INFO)

# Configuration parameters
config = {
    'traffic_monitoring': True,  # Enable traffic monitoring
    'resource_monitoring': True,  # Enable resource monitoring
}

# Function to monitor server resource usage
def monitor_resources():
    if config['resource_monitoring']:
        # Monitor CPU usage using psutil
        cpu_percent = psutil.cpu_percent(interval=1)
        logging.info(f'CPU Usage: {cpu_percent}%')

# Function to log traffic statistics
def log_traffic(data_received, data_sent):
    if config['traffic_monitoring']:
        logging.info(f'Total data received: {data_received} bytes')
        logging.info(f'Total data sent: {data_sent} bytes')

def main(local_tunnel, remote_host, remote_port):
    tss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tss.bind(local_tunnel)

    tss.listen(1)

    tsock = None

    lastping = time.time()

    total_data_received = 0  # Track total data received
    total_data_sent = 0      # Track total data sent

    while True:
        r = [tss, tsock]
        w = []
        e = []

        if tsock is not None:
            r.append(tsock)
            e.append(tsock)

        r, w, e = select.select(r, w, e, 1)

        if time.time() - lastping > 5:
            lastping = time.time()
            if tsock is not None:
                # Send a little ping to help the client
                # determine when the connection has dropped
                # and it needs to be re-established
                try:
                    tsock.send(struct.pack('>B', 3))
                except socket.error as se:
                    logging.error(f"Error sending ping: {str(se)}")
                    # Handle the socket error gracefully, e.g., close the socket

        if tss in r:
            logging.info('Local tunnel connection')
            try:
                tsock, addr = tss.accept()
                r.remove(tss)
            except socket.error as se:
                logging.error(f"Error accepting local tunnel connection: {str(se)}")
                # Handle the socket error gracefully, e.g., close the socket

        if tsock in e:
            try:
                tsock.close()
                tsock = None
            except socket.error as se:
                logging.error(f"Error closing local tunnel connection: {str(se)}")
                # Handle the socket error gracefully

        if tsock is not None:
            # Receive data from the local tunnel
            try:
                data = tsock.recv(4096)
            except ConnectionResetError:
                logging.error('Local tunnel connection reset error')
                data = False

            if not data:
                logging.info('Local tunnel dropped')
                tsock.close()
                tsock = None
                continue

            # Send data to the remote host
            try:
                remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                remote_socket.connect((remote_host, remote_port))
                remote_socket.sendall(data)

                while True:
                    response = remote_socket.recv(4096)
                    if not response:
                        break
                    tsock.sendall(response)

                remote_socket.close()

                total_data_sent += len(data)
                total_data_received += len(data)

            except socket.error as se:
                logging.error(f"Error forwarding data to remote host: {str(se)}")

        # Log traffic statistics
        log_traffic(total_data_received, total_data_sent)

        # Monitor server resource usage
        monitor_resources()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Tunnel Server')
    parser.add_argument('--log-level', dest='log_level', default='INFO', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        help='Set the logging level (default: INFO)')
    parser.add_argument('local_tunnel_port', type=int, help='Port for local tunnel connection')
    parser.add_argument('remote_host', type=str, help='Remote host to forward data to')
    parser.add_argument('remote_port', type=int, help='Remote port to forward data to')
    args = parser.parse_args()

    # Configure logging level based on command-line argument
    log_level = getattr(logging, args.log_level)
    logging.basicConfig(filename='tunnel_server.log', level=log_level)

    local_tunnel = ('0.0.0.0', args.local_tunnel_port)
    remote_host = args.remote_host
    remote_port = args.remote_port

    main(local_tunnel, remote_host, remote_port)
