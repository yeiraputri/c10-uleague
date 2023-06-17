from django.urls import path
from mulai_pertandingan.views import show_mulai_pertandingan, show_pilih_peristiwa

app_name = 'dashboard'

urlpatterns = [
    path('mulai_pertandingan/', show_mulai_pertandingan, name='show_mulai_pertandingan'),
    path('pilih_peristiwa/', show_pilih_peristiwa, name='show_pilih_peristiwa'),
]