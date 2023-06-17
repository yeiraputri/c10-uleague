from django.urls import path
from mengelola_tim.views import form_daftar_tim, list_tim, daftar_pelatih, daftar_pemain

app_name = 'mengelola_tim'

urlpatterns = [
    path('', form_daftar_tim, name='form_daftar_tim'),
    path('list_tim', list_tim, name='list_tim'),
    path('daftar_pelatih', daftar_pelatih, name='daftar_pelatih'),
    path('daftar_pemain', daftar_pemain, name='daftar_pemain'),
]