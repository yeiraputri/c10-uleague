import re
from django.shortcuts import redirect, render
from utils.query import query


# Create your views here.
#def manage_pertandingan(request):
#    return render(request, 'manage_pertandingan.html')

def manage_pertandingan(request):
    role = request.COOKIES.get('role')

    if role == None:
        return redirect('home:login')
    if role != "PANITIA":
        return redirect('home:home')
    
    month_translations = {
    "January": "Januari",
    "February": "Februari",
    "March": "Maret",
    "April": "April",
    "May": "Mei",
    "June": "Juni",
    "July": "Juli",
    "August": "Agustus",
    "September": "September",
    "October": "Oktober",
    "November": "November",
    "December": "Desember"
    }
    
    list_pertandingan, err = query("select * from pertandingan")
    # print(type(list_pertandingan))
    info_pertandingan = []
    for i in range(len(list_pertandingan)):

        tim, err = query(f"select distinct tm.nama_tim from tim_pertandingan tm, pertandingan p where tm.id_pertandingan = '{list_pertandingan[i][0]}'  ")

        tim = f"{tim[0][0]} vs {tim[1][0]}"

        stadium, err = query(f"select distinct s.nama from stadium s, pertandingan p where s.id_stadium = '{list_pertandingan[i][3]}' ")

        stadium = stadium[0][0]

        waktu = list_pertandingan[i][1]
        waktu = waktu.strftime("%d %B %Y, %H:%M")
        
        for month in month_translations:
            if month in waktu:
                translated_month = month_translations[month]
                waktu = re.sub(r'\b{}\b'.format(month), translated_month, waktu)
                    
        id_pertandingan = list_pertandingan[i][0]

        info_pertandingan.append([id_pertandingan, tim, stadium, waktu])
    
    context = {
        "info_pertandingan": info_pertandingan,
        "role": role
    }
    
    return render(request, 'manage_pertandingan.html', context)


""" def manage_pertandingan(request):
    role = request.COOKIES.get('role')

    if role == None:
        return redirect('home:login')
    if role != "PANITIA":
        return redirect('home:home')
    
    context = {
        "role": role
    }

    
    return render(request, 'manage_pertandingan.html', context) """