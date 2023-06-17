import re
from django.shortcuts import redirect, render

from utils.query import query

# Create your views here.
def manajer_dashboard(request):
    role = request.COOKIES.get("role")
    id_manajer = request.COOKIES.get("userId")

    if role == None:
        return redirect('home:login')
    if role != "MANAJER":
        return redirect('home:home')
    
    info_user, err = query(f"select concat (np.nama_depan, ' ', np.nama_belakang), np.nomor_hp, np.email, np.alamat, snp.status from non_pemain np, status_non_pemain snp where np.id = snp.id_non_pemain and np.id = '{id_manajer}';")
    daftar_pemain, err = query(f"select concat (p.nama_depan, ' ', p.nama_belakang) as nama_lengkap, is_captain, posisi  from pemain p where p.nama_tim = (select tm.nama_tim from tim_manajer tm where tm.id_manajer = '{id_manajer}')")
    context = {
        'role': role,
        'daftar_pemain': daftar_pemain,
        'info_user': info_user[0]
    }

    return render(request, 'manajer_dashboard.html', context)

def panitia_dashboard(request):
    role = request.COOKIES.get("role")
    id_panitia = request.COOKIES.get("userId")
    info_user, err = query(f"select concat (np.nama_depan, ' ', np.nama_belakang), np.nomor_hp, np.email, np.alamat, snp.status, jabatan from non_pemain np, status_non_pemain snp, panitia p where np.id = snp.id_non_pemain and p.id_panitia = np.id and np.id = '{id_panitia}';")

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
    info_pertandingan = []
    for i in range(len(list_pertandingan)):

        tim_bertanding, err = query(f"select distinct tm.nama_tim from tim_pertandingan tm, pertandingan p where tm.id_pertandingan = '{list_pertandingan[i][0]}'  ")

        tim_bertanding = f"{tim_bertanding[0][0]} vs {tim_bertanding[1][0]}"

        stadium, err = query(f"select distinct s.nama from stadium s, pertandingan p where s.id_stadium = '{list_pertandingan[i][3]}' ")

        stadium = stadium[0][0]

        start_time = list_pertandingan[i][1]
        start_time = start_time.strftime("%d %B %Y, %H:%M")
        
        for month in month_translations:
            if month in start_time:
                translated_month = month_translations[month]
                start_time = re.sub(r'\b{}\b'.format(month), translated_month, start_time)
                    
        id_pertandingan = list_pertandingan[i][0]

        info_pertandingan.append([id_pertandingan, tim_bertanding, stadium, start_time])
    
    context = {
        "info_pertandingan": info_pertandingan,
        "role": role,
        "info_user": info_user[0]
    }
    
    return render(request, 'panitia_dashboard.html', context)

def penonton_dashboard(request):
    role = request.COOKIES.get('role')
    id_penonton = request.COOKIES.get('userId')
    info_user, err = query(f"select concat (np.nama_depan, ' ', np.nama_belakang), np.nomor_hp, np.email, np.alamat, snp.status from non_pemain np, status_non_pemain snp where np.id = snp.id_non_pemain and np.id = '{id_penonton}';")

    if role == None:
        return redirect('home:login')
    if role != "PENONTON":
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
    
    list_pertandingan, err = query(f"select * from pertandingan where id_pertandingan = (select pt.id_pertandingan from pembelian_tiket pt where id_penonton = '{id_penonton}')")
    info_pertandingan = []
    for i in range(len(list_pertandingan)):


        tim_bertanding, err = query(f"select distinct tm.nama_tim from tim_pertandingan tm, pertandingan p where tm.id_pertandingan = '{list_pertandingan[i][0]}'  ")

        tim_bertanding = f"{tim_bertanding[0][0]} vs {tim_bertanding[1][0]}"

        stadium, err = query(f"select distinct s.nama from stadium s, pertandingan p where s.id_stadium = '{list_pertandingan[i][3]}' ")

        stadium = stadium[0][0]

        start_time = list_pertandingan[i][1]
        start_time = start_time.strftime("%d %B %Y, %H:%M")
        
        for month in month_translations:
            if month in start_time:
                translated_month = month_translations[month]
                start_time = re.sub(r'\b{}\b'.format(month), translated_month, start_time)
                    

        end_time = list_pertandingan[i][2]
        end_time = end_time.strftime("%H:%M")

        info_pertandingan.append([tim_bertanding, stadium, start_time, end_time])
    
    context = {
        "info_pertandingan": info_pertandingan,
        "role": role,
        "info_user": info_user[0]
    }
   
    return render(request, 'penonton_dashboard.html', context)