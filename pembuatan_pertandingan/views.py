from django.shortcuts import render

# Create your views here.
def pembuatan_pertandingan(request):
    return render(request, 'pembuatan_pertandingan.html')

def pemilihan_waktu(request):
    return render(request, 'pemilihan_waktu.html')

def buat_pertandingan(request):
    return render(request, 'buat_pertandingan.html')