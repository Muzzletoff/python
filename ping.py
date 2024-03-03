import ping3

def ping_target(target_ip):
    try:
        pinger = ping3.Ping()
        rtt = pinger.ping(target_ip)
        if rtt is not None:
            return rtt * 1000  # Convert to milliseconds
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    target_ip = input("Enter the target IP address or hostname: ")
    print(f"Pinging {target_ip}...")

    while True:
        rtt = ping_target(target_ip)
        if rtt is not None:
            print(f"Round-Trip Time: {rtt:.2f} ms")
        else:
            print("Ping failed")

if __name__ == "__main__":
    main()
