from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse


def backend_view(request):
    return JsonResponse({'info': "Hello, You're at the backend view."})
