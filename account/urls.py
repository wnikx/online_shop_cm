from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


app_name = 'account'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]
