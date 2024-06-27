from scapy.all import rdpcap

# read_pcap will read and extract information from a layer
# of a packet that has layers

def read_pcap(file_path):
    packets = rdpcap(file_path)
    packet_details = []
    for packet in packets:
        if packet.haslayer('IP'):
            details = {
                'timestamp': packet.time,
                'source_ip': packet['IP'].src,
                'destination_ip': packet['IP'].dst,
                'protocol': packet['IP'].proto,
                'payload': str(packet['IP'].payload)
            }
            packet_details.append(details)
    return packet_details

