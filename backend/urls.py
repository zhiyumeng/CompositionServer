from django.urls import path

from . import views

urlpatterns = [
    # ex:/backend
    path('', views.backend_view, name='backend_view'),
    # ex: /backend/1
    path('user/<int:user_id>', views.get_user_info)
]
