from scapy.all import sniff, wrpcap
# Define a callback function to analyze captured packets
def analyze_packet(packet):
# Extract information from the packet header
Source_ip = packet[IP].src
destination_ip = packet[IP].dst
protocol = packet[IP].proto
# Print basic information about the packet
print(f"Source IP: {source_ip} -> Destination IP: {destination_ip} (Protocol: {protocol})")
# Add custom logic here to analyze specific protocols (e.g., HTTP, TCP flags)
# Capture network traffic and call the callback function for each packet
sniff(prn=analyze_packet, filter="ip", capture_offline=False) # Replace "capture_offline=False"
with a PCAP file path for offline analysis
# Example usage for offline analysis (replace "traffic.pcap" with your file path)
# wrpcap("traffic.pcap", sniff(offline="traffic.pcap", filter="ip"))
