from django.urls import path
from peminjaman_stadium.views import *

app_name = 'peminjaman_stadium'

urlpatterns = [
    path('', peminjaman_stadium, name='peminjaman_stadium'),
    path('pilih_stadium/', pilih_stadium, name='pilih_stadium'),
    path('update_peminjaman/', update_peminjaman, name='update_peminjaman'),
    # path('list_waktu_stadium/', list_waktu_stadium, name='list_waktu_stadium')
]