from django.urls import path
from mulai_rapat.views import pilih_pertandingan, rapat_pertandingan
app_name = 'mulai_rapat'

urlpatterns = [
    path('', pilih_pertandingan, name='pilih_pertandingan'),
    path('rapat_pertandingan/<uuid:id>', rapat_pertandingan, name='rapat_pertandingan'),

]