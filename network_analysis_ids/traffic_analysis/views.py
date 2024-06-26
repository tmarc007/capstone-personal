from django.conf import settings
from django.shortcuts import render, redirect
from .forms import PcapFileForm
from .models import PcapFile
from .utils import read_pcap
import os

def index(request):
    return render(request, 'base.html', {})

def upload_view(request):
    return render(request, 'upload.html', {})

def results_view(request):
    return render(request, 'results.html', {})


def upload_files(request):
    if request.method == 'POST':
        form = PcapFileForm(request.POST, request.FILES)
        if form.is_valid():
            pcap_file = form.save()
            return redirect('analyze_traffic', pcap_file_id=pcap_file.id)
    else:
        form = PcapFileForm()
    return render(request, 'traffic_analysis/upload.html', {'form': form})

def analyze_traffic(request, pcap_file_id):
    pcap_file = PcapFile.objects.get(id=pcap_file_id)
    file_path = pcap_file.file.path
    packets = read_pcap(file_path)
    return render(request, 'traffic_analysis/results.html', {'packets': packets})
