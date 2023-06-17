from django.shortcuts import render

# Create your views here.
def pengguna(request):
    return render(request, 'pengguna_register.html')

def register_manajer_penonton(request):
    return render(request, 'register_manajer_penonton.html')

def register_panitia(request):
    return render(request, 'register_panitia.html')