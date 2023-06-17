from django.urls import path
from pengguna.views import pengguna, register_manajer_penonton, register_panitia

app_name = 'pengguna'

urlpatterns = [
    path('', pengguna, name='pengguna'),
    path('register_manajer_penonton', register_manajer_penonton, name='register_manajer_penonton'),
    path('register_panitia', register_panitia, name='register_panitia'),
]