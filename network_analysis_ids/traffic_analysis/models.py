from django.db import models

class PcapFile(models.Model):
    file = models.FileField(upload_to='pcap_files/')
    upload_at = models.DateTimeField(auto_now_add=True)