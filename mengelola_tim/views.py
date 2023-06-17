from django.shortcuts import redirect, render
from utils.query import query
import re

# Create your views here.

def form_daftar_tim(request):
    role = request.COOKIES.get('role')

    if role == None:
        return redirect('home:login')
    if role not in ["MANAJER"]:
        return redirect('home:home')
    
    if request.method == "POST":
        nama_tim = request.POST.get('nama_tim')
        universitas = request.POST.get('universitas')

        list_tim, err = query(f"SELECT * FROM TIM WHERE nama_tim = '{nama_tim}' AND universitas = '{universitas}';")
        print(list_tim)
        context = {
            "role": role,
        }
    
        return render(request, 'form_daftar_tim.html', context)
    
    else:
        print("gajelas")

        context = {
            "role": role,
        }
    
        return render(request, 'form_daftar_tim.html', context)

def list_tim(request):
    role = request.COOKIES.get('role')

    if role == None:
        return redirect('home:login')
    if role not in ["MANAJER"]:
        return redirect('home:home')
    

    context = {
        "role": role
    }

    return render(request, 'list_tim.html', context)

def daftar_pemain(request):
    role = request.COOKIES.get('role')

    if role == None:
        return redirect('home:login')
    if role not in ["MANAJER"]:
        return redirect('home:home')
    
    context = {
        "role": role
    }
    return render(request, 'daftar_pemain.html', context)

def daftar_pelatih(request):
    role = request.COOKIES.get('role')

    if role == None:
        return redirect('home:login')
    if role not in ["MANAJER"]:
        return redirect('home:home')
    
    context = {
        "role": role
    }
    return render(request, 'daftar_pelatih.html', context)


