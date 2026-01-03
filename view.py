import requests
from django.http import JsonResponse

def analyze_resume(request):
    file = request.FILES['resume']
    job = request.POST['job']

    response = requests.post(
        "http://127.0.0.1:8001/analyze/",
        files={"file": file},
        data={"job": job}
    )

    return JsonResponse(response.json())
