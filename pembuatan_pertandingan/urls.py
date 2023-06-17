from django.urls import path
from pembuatan_pertandingan.views import pembuatan_pertandingan, pemilihan_waktu, buat_pertandingan

app_name = 'pembuatan_pertandingan'

urlpatterns = [
    path('', pembuatan_pertandingan, name='pembuatan_pertandingan'),
    path('pemilihan_waktu/', pemilihan_waktu, name='pemilihan_waktu'),
    path('buat_pertandingan/', buat_pertandingan, name="buat_pertandingan")
]