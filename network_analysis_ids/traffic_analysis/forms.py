from django import forms
from .models import PcapFile

# This form will be used to upload pcap files based on the PcapFile model
class PcapFileForm(forms.ModelForm):
    class Meta:
        model = PcapFile
        fields = ['file']
