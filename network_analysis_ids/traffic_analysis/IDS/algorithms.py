from .models import NetworkPacket, IDSAlert

def detect_anomalies():
    #Fetch  all TCP(transmission control protocol) packets
    suspicious_packets = NetworkPacket.object.filter(protocol='TCP')

    for packet in suspicious_packets:
        # Check for abnormal packet size 
        if len(packet.payload) > 1000:
            # Create an IDS alert
            IDSAlert.objects.create(
                alert_type='Abnormal Packet Size',
                description=f'TCP packet from {packet.source_ip} with payload {len(packet.payload)}',
                severity=3
            )

        if 'malicious_pattern' in packet.payload:
            IDSAlert.objects.create(
                alert_type='Malicious Pattern Detected',
                description='TCP packet from {packet.source_ip} matched a malicious pattern', 
                severity=5
            )

            # we can add more detection rules as the team sees fit

    return True