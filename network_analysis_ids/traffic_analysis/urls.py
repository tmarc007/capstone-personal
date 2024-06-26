from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_files, name='upload_files'),
    path('results/', views.results_view, name='results'),
    path('analyze/<int:pcap_file_id>/', views.analyze_traffic, name='analyze_traffic'),
]