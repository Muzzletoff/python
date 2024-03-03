import sys
from scapy.all import sniff

def packet_handler(packet):
    print(packet.summary())

def main(interface="wlan0"):
    print(f"Sniffing on interface {interface}. Press Ctrl+C to stop.")
    try:
        sniff(iface=interface, prn=packet_handler, store=False)
    except KeyboardInterrupt:
        print("Sniffing stopped.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
