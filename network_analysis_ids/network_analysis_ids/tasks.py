from celery import shared_task
from scapy.all import sniff
from .models import NetworkPacket, IDSAlert

@shared_task
def monitor_traffic_realtime():
    # Callback function to process each captured packet
    def process_packet(packet):
        try:
            packet_data = {
                'source_ip': packet[0][1].src,
                'destination_ip': packet[0][1].dst,
                'protocol': packet[0][1].proto,
                'payload': str(packet)
            }
            NetworkPacket.objects.create(**packet_data)
            
            # anomaly detection
            if packet[0][1].proto == 6:  # TCP protocol
                IDSAlert.objects.create(
                    alert_type="Suspicious TCP Packet",
                    description=f"Suspicious TCP packet from {packet[0][1].src} to {packet[0][1].dst}",
                    severity=5
                )
        except Exception as e:
            # Handle exceptions, can't think of any
            pass

    # Start sniffing packets and call process_packet for each captured packet
    sniff(prn=process_packet, store=0)




