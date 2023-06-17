import re
from django.shortcuts import redirect, render
from utils.query import query
# Create your views here.
""" def show_mulai_pertandingan(request):
    return render(request, 'mulai_pertandingan.html')

def show_pilih_peristiwa(request):
    return render(request, 'pilih_peristiwa.html')
 """
def mulai_pertandingan(request):
    role = request.COOKIES.get('role')

    if role == None:
        return redirect('home:login')
    if role != "PANITIA":
        return redirect('home:home')
    
    
    list_pertandingan, err = query("select * from pertandingan")
    # print(type(list_pertandingan))
    info_pertandingan = []
    for i in range(len(list_pertandingan)):

        tim1, err = query(f"select distinct tm.nama_tim from tim_pertandingan tm, pertandingan p where tm.id_pertandingan = '{list_pertandingan[i][0]}'  ")

        tim1 = f"{tim1[0][0]}"

        tim2, err = query(f"select distinct tm.nama_tim from tim_pertandingan tm, pertandingan p where tm.id_pertandingan = '{list_pertandingan[i+1][0]}'  ")

        tim2 = f"{tim2[0][0]}"
                   
        id_pertandingan = list_pertandingan[i][0]

        info_pertandingan.append([id_pertandingan, tim1, tim2])
    
    context = {
        "info_pertandingan": info_pertandingan,
        "role": role
    }
    
    return render(request, 'mulai_pertandingan.html', context)

def pilih_peristiwa(request):
    role = request.COOKIES.get('role')

    if role == None:
        return redirect('home:login')
    if role != "PANITIA":
        return redirect('home:home')
    
    
    list_tim, err = query("select * from tim")
    # print(type(list_pertandingan))
    info_tim = []
    for i in range(len(list_tim)):

        nama_pemain, err = query(f"select distinct p.nama_pemain from pemain p, tim t where p.nama_tim = '{list_tim[i][0]}'  ")

        nama_pemain = f"{nama_pemain[0][0]}"

        """ peristiwa, err = query(f"select distinct tm.nama_tim from tim_pertandingan tm, pertandingan p where tm.id_pertandingan = '{list_pertandingan[i+1][0]}'  ")

        peristiwa = f"{peristiwa[0][0]}"
                   
        id_pertandingan = list_pertandingan[i][0] """

        info_tim.append([nama_tim, nama_pemain, peristiwa])
    
    context = {
        "info_pertandingan": info_tim,
        "role": role
    }
    return render(request, 'pilih_peristiwa.html', context)

