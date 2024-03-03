import subprocess

def list_wifi_networks():
    try:
        # Run the nmcli command to list Wi-Fi connections
        result = subprocess.check_output(["nmcli", "device", "wifi", "list"], universal_newlines=True)
        
        # Split the result by lines and count the number of networks
        networks = result.strip().split('\n')[1:]  # Skip the header line
        num_networks = len(networks)
        
        # Print the list of networks with auto-incremented numbers
        print(f"Number of available Wi-Fi networks: {num_networks}")
        print("Available Wi-Fi networks:")
        for idx, network in enumerate(networks, start=1):
            print(f"{idx}. {network}")
    except FileNotFoundError:
        print("Error: nmcli command not found. This script is intended for Linux systems with NetworkManager.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_wifi_networks()
