from django.urls import path
from home.views import *

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('login_register/', login_register, name='login_register'),
    path('register/', register, name='register'),
    path('register_manajer/', register_manajer, name='register_manajer'),
    path('register_penonton/', register_penonton, name='register_penonton'),
    path('register_panitia/', register_panitia, name='register_panitia'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]