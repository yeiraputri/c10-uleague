from django.urls import path
from manage_pertandingan.views import manage_pertandingan

app_name = 'manage_pertandingan'

urlpatterns = [
    path('', manage_pertandingan, name='manage_pertandingan'),
]