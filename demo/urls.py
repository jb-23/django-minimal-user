from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('error', views.home, {'error': True}, name='error'),
]
