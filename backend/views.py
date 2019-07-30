from django.shortcuts import render

# Create your views here.
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .models import User


def backend_view(request):
    return JsonResponse({'info': "Hello, You're at the backend view."})


def get_user_info(request, user_id):
    user = User.objects.filter(id=user_id)
    user = user[0]
    return JsonResponse({'status': 0, 'name':user.name,'user_id':user.id,'tel':user.tel_number})
