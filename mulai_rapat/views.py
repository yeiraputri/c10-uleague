import re
from django.contrib import messages
from django.shortcuts import redirect, render
from mulai_rapat.forms import IsiRapat
from utils.query import query
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def pilih_pertandingan(request):
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
        "role": role
    }
    
    return render(request, 'pilih_pertandingan.html', context)

@csrf_exempt
def rapat_pertandingan(request, id):
    role = request.COOKIES.get('role')

    if role == None:
        return redirect('home:login')
    if role != "PANITIA":
        return redirect('home:home')
    
    tim_bertanding, err = query(f"select distinct tm.nama_tim from tim_pertandingan tm, pertandingan p where tm.id_pertandingan = '{id}'  ")
    tim_bertanding = f"{tim_bertanding[0][0]} vs {tim_bertanding[1][0]}"
    isi_rapat = query(f"select isi_rapat from rapat where id_pertandingan = '{id}' ")
    isi_rapat = isi_rapat[0][0][0]
    context = {
        "role": role,
        "tim_bertanding": tim_bertanding,
        "isi_rapat": isi_rapat
    }

    if request.method == "POST":
        # ambil data dari textfield, kemudian post ke postgres sql
        form = IsiRapat(request.POST)
        if form.is_valid():
            isi_rapat = form.cleaned_data.get("desc_rapat"),
            print(isi_rapat)
            datetime, err = query(f"select start_datetime from pertandingan where id_pertandingan = '{id}'")
            id_panitia, err = query(f"select id_panitia from panitia where username = '{request.COOKIES.get('username')}'")
            tim_bertanding, err = query(f"select distinct tm.nama_tim from tim_pertandingan tm, pertandingan p where tm.id_pertandingan = '{id}'  ")
            id_manajer_tim_a, err = query(f"select id_manajer from tim_manajer where nama_tim = '{tim_bertanding[0][0]}'")
            id_manajer_tim_b, err = query(f"select id_manajer from tim_manajer where nama_tim = '{tim_bertanding[1][0]}'")
            query(f"insert into rapat values('{id}', '{datetime[0][0]}', '{id_panitia[0][0]}', '{id_manajer_tim_a[0][0]}', '{id_manajer_tim_b[0][0]}', '{isi_rapat[0]}')")
            messages.success(request, "Isi Rapat Berhasil dibuat!")
            return redirect('mulai_rapat:pilih_pertandingan')

    return render(request, 'rapat_pertandingan.html', context)
