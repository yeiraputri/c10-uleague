from django.shortcuts import redirect, render

from utils.query import query
import datetime
import re

# Create your views here.
# def history_rapat(request):
#     role = request.COOKIES.get('role')

#     if role == None:
#         return redirect('home:login')
#     if role not in ["MANAJER"]:
#         return redirect('home:home')
    
#     month_translations = {
#     "January": "Januari",
#     "February": "Februari",
#     "March": "Maret",
#     "April": "April",
#     "May": "Mei",
#     "June": "Juni",
#     "July": "Juli",
#     "August": "Agustus",
#     "September": "September",
#     "October": "Oktober",
#     "November": "November",
#     "December": "Desember"
#     }
    
#     list_pertandingan, err = query("select * from pertandingan")
#     list_rapat, err = query("select * from rapat")
#     # print(type(list_pertandingan))
#     info_rapat = []
#     for i in range(len(list_pertandingan)):


#         tim_rapat, err = query(f"select distinct tm.nama_tim from tim_pertandingan tm, pertandingan p where tm.id_pertandingan = '{list_pertandingan[i][0]}'  ")

#         tim_rapat = f"{tim_rapat[0][0]} vs {tim_rapat[1][0]}"

#         stadium, err = query(f"select distinct s.nama from stadium s, pertandingan p where s.id_stadium = '{list_pertandingan[i][3]}' ")

#         stadium = stadium[0][0]

#         start_time = list_pertandingan[i][1]
#         start_time = start_time.strftime("%d %B %Y, %H:%M")
        
#         for month in month_translations:
#             if month in start_time:
#                 translated_month = month_translations[month]
#                 start_time = re.sub(r'\b{}\b'.format(month), translated_month, start_time)
                    

#         end_time = list_pertandingan[i][2]
#         end_time = end_time.strftime("%H:%M")

#         nama_panitia, err = query(f"SELECT CONCAT(np.nama_depan, ' ', np.nama_belakang) FROM non_pemain np JOIN panitia p ON p.id_panitia = np.id JOIN rapat r ON r.perwakilan_panitia = p.id_panitia where p.id_panitia = '{list_rapat[i][2]}'")
#         nama_panitia = nama_panitia[0][0]
#         laporan_rapat, err = query(f"select isi_rapat from rapat where id_pertandingan = '{list_pertandingan[i][0]}'")
#         info_rapat.append([tim_rapat, nama_panitia, stadium, start_time, end_time, laporan_rapat[0][0]])
        
#     context = {
#         "info_rapat": info_rapat,
        
#         "role": role

#     }
   
#     return render(request, 'history_rapat.html', context)

# def isi_rapat(request,isi):
#     role = request.COOKIES.get('role')

#     if role == None:
#         return redirect('home:login')
#     if role not in ["MANAJER"]:
#         return redirect('home:home')
#     context = {
#         "isi_rapat": isi,
#         "role": role
#     }
#     return render(request, 'isi_rapat.html', context)

def history_rapat(request):
    role = request.COOKIES.get('role')

    if role == None:
        return redirect('home:login')
    if role not in ["MANAJER"]:
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
    
    id_manajer = request.COOKIES.get('userId')

    checked = []
    
    list_rapat_all, err = query(f"select manajer_tim_a, manajer_tim_b, p.id_pertandingan, stadium, start_datetime, end_datetime, perwakilan_panitia, isi_rapat  from pertandingan p join tim_pertandingan tp on p.id_pertandingan = tp.id_pertandingan  join tim_manajer tm on tp.nama_tim = tm.nama_tim join rapat r on r.id_pertandingan = p.id_pertandingan where r.manajer_tim_a = '{id_manajer}'  and tp.nama_tim = tm.nama_tim")

    # print(list_rapat_all)
    # print(type(list_pertandingan))
    info_rapat = []
    if len(list_rapat_all) != 0:
        for i in range(len(list_rapat_all)):
            if list_rapat_all[i][0] not in checked:
                # print(list_rapat_all[0])
                id_manajer_a = list_rapat_all[i][0]
                id_manajer_a = str(id_manajer_a)
                id_manajer_b = list_rapat_all[i][1]
                id_manajer_b = str(id_manajer_b)
                tim_rapat_a, err = query(f"select nama_tim from tim_manajer where id_manajer = '{id_manajer_a}'")
                tim_rapat_a = tim_rapat_a[0][0]

                tim_rapat_b, err = query(f"select nama_tim from tim_manajer where id_manajer = '{id_manajer_b}'")
                tim_rapat_b = tim_rapat_b[0][0]

                tim_rapat = f"{tim_rapat_a} vs {tim_rapat_b}"

                print([tim_rapat_a, tim_rapat_b])
                print(id_manajer_a)
                print(id_manajer_b)

                id_panitia = list_rapat_all[i][6]
                
                nama_panitia, err = query(f"SELECT CONCAT(np.nama_depan, ' ', np.nama_belakang) FROM non_pemain np JOIN panitia p ON p.id_panitia = np.id JOIN rapat r ON r.perwakilan_panitia = p.id_panitia where p.id_panitia = '{id_panitia}'")
                nama_panitia = nama_panitia[0][0]
                print(nama_panitia)

                id_stadium = list_rapat_all[i][3]
                stadium, err = query(f"select distinct s.nama from stadium s, pertandingan p where s.id_stadium = '{list_rapat_all[i][3]}' ")
                stadium = stadium[0][0]
                print(stadium)

                start_time = list_rapat_all[i][4]
                start_time = start_time.strftime("%d %B %Y, %H:%M")
                
                for month in month_translations:
                    if month in start_time:
                        translated_month = month_translations[month]
                        start_time = re.sub(r'\b{}\b'.format(month), translated_month, start_time)
                            

                end_time = list_rapat_all[i][5]
                end_time = end_time.strftime("%H:%M")

                print([start_time, end_time])
                isi_rapat = list_rapat_all[i][7]
                print(isi_rapat)
                info_rapat.append([tim_rapat, nama_panitia, stadium, start_time, end_time, isi_rapat])

                checked.append(list_rapat_all[i][0])

    
    

        
        
    context = {
        "info_rapat": info_rapat,
        
        "role": role

    }
   
    return render(request, 'history_rapat.html', context)

def isi_rapat(request,isi):
    role = request.COOKIES.get('role')

    if role == None:
        return redirect('home:login')
    if role not in ["MANAJER"]:
        return redirect('home:home')
    context = {
        "isi_rapat": isi,
        "role": role
    }
    return render(request, 'isi_rapat.html', context)