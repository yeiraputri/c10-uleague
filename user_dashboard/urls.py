from django.urls import path
from user_dashboard.views import manajer_dashboard, panitia_dashboard, penonton_dashboard

app_name = 'user_dashboard'

urlpatterns = [
    path('manajer_dashboard/', manajer_dashboard, name='manajer_dashboard'),
    path('panitia_dashboard/', panitia_dashboard, name='panitia_dashboard'),
    path('penonton_dashboard/', penonton_dashboard, name='penonton_dashboard'),
]
