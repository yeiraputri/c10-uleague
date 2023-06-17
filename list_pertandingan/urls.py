from django.urls import path
from list_pertandingan.views import list_pertandingan

app_name = 'list_pertandingan'

urlpatterns = [
    path('', list_pertandingan, name='list_pertandingan'),
]