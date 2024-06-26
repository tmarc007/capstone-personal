from django.http import JsonResponse
from .algorithms import detect_anomalies

# If the request method is post then run detect_anomalies from algorithms.py 
def detect_anomalies_api(request):
    if request.method == 'POST':
        result = detect_anomalies()
        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
