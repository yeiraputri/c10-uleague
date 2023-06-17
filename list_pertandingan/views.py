from django.shortcuts import redirect, render
from utils.query import query
import datetime
import re

# Create your views here.
# def list_pertandingan(request):
#     role = request.COOKIES.get('role')

#     if role == None:
#         return redirect('home:login')
#     if role not in ["PENONTON", "MANAJER"]:
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
#     # print(type(list_pertandingan))
#     info_pertandingan = []

#     if role == "MANAJER":
#         id_manajer = request.COOKIES.get('userId')
#         check_q1 = f"select nama_tim from tim_manajer where id_manajer = '{id_manajer}' "
#         q1,err = query(f"select nama_tim from tim_manajer where id_manajer = '{id_manajer}' ")
#         print(q1)
#         q2,err = query(f"select id_pertandingan from tim_pertandingan where nama_tim = '{q1[0][0]}'")
#         q2 = str(q2[0][0])
#         print(q2)

#         tim_bertanding , err = query(f"select nama_tim from tim_pertandingan where id_pertandingan = '{q2}'")
#         print(tim_bertanding)

#         tim_bertanding = f"{tim_bertanding[0][0]} vs {tim_bertanding[1][0]}"
#         list_pertandingan, err = query(f"select * from pertandingan where id_pertandingan = '{q2}'")
#         for i in range(len(list_pertandingan)):

#     for i in range(len(list_pertandingan)):

#         if role == "PENONTON":
#             print("MASUK PENONTON")
#             tim_bertanding, err = query(f"select distinct tm.nama_tim from tim_pertandingan tm, pertandingan p where tm.id_pertandingan = '{list_pertandingan[i][0]}'  ")
#         else:
#             print("MASUK MANAJER")
#             id_manajer = request.COOKIES.get('userId')
#             # q4 = f"select distinct tm.nama_tim from tim_pertandingan tm, pertandingan p, tim_manajer tmm where tm.id_pertandingan = '{list_pertandingan[i][0]}' and  tmm.id_manajer = '{id_manajer}'"
#             # tim_bertanding, err = query(q4);
#             # print(q4)
#             # print(tim_bertanding)
#             check_q1 = f"select nama_tim from tim_manajer where id_manajer = '{id_manajer}' "
#             q1,err = query(f"select nama_tim from tim_manajer where id_manajer = '{id_manajer}' ")
#             print(q1)
#             q2,err = query(f"select id_pertandingan from tim_pertandingan where nama_tim = '{q1[0][0]}'")
#             q2 = str(q2[0][0])
#             print(q2)

#             tim_bertanding , err = query(f"select nama_tim from tim_pertandingan where id_pertandingan = '{q2}'")
#             print(tim_bertanding)

#             tim_bertanding = f"{tim_bertanding[0][0]} vs {tim_bertanding[1][0]}"

#             check_query = f"select distinct s.nama from stadium s, pertandingan p where s.id_stadium = '{list_pertandingan[i][3]}' and p.id_pertandingan = '{q2}' and p.stadium = '{list_pertandingan[i][3]}'"
#             print(check_query)
#             stadium, err = query(check_query)

#             print(stadium)

#             stadium = stadium[0][0]

#             start_time = list_pertandingan[i][1]
#             start_time = start_time.strftime("%d %B %Y, %H:%M")
            
#             for month in month_translations:
#                 if month in start_time:
#                     translated_month = month_translations[month]
#                     start_time = re.sub(r'\b{}\b'.format(month), translated_month, start_time)
                        

#             end_time = list_pertandingan[i][2]
#             end_time = end_time.strftime("%H:%M")

#             info_pertandingan.append([tim_bertanding, stadium, start_time, end_time])

#         tim_bertanding = f"{tim_bertanding[0][0]} vs {tim_bertanding[1][0]}"

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

#         info_pertandingan.append([tim_bertanding, stadium, start_time, end_time])
    
#     context = {
#         "info_pertandingan": info_pertandingan,
#         "role": role
#     }

#     print(info_pertandingan[1])
   
#     return render(request, 'list_pertandingan.html', context)

def list_pertandingan(request):
    role = request.COOKIES.get('role')

    if role == None:
        return redirect('home:login')
    if role not in ["PENONTON", "MANAJER"]:
        return redirect('home:home')

    info_pertandingan = []
    if role == "MANAJER":

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
        
        list_pertandingan, err = query(f"select * from pertandingan p join tim_pertandingan tp on p.id_pertandingan = tp.id_pertandingan join tim_manajer tm on tp.nama_tim = tm.nama_tim where tm.id_manajer = '{id_manajer}' and tp.nama_tim = tm.nama_tim")
        print((list_pertandingan))
        
        if len(list_pertandingan) != 0:
            info_pertandingan = []
            # tim bertanding, stadium, starttime date time
            for i in range (len(list_pertandingan)):
                stadium = str(list_pertandingan[i][3])
                # print(stadium)
                stadium, err = query(f"select nama from stadium where id_stadium = '{stadium}'")
                stadium_name = stadium[0][0]
                print(stadium_name)

                start_time = list_pertandingan[i][1]
                start_time = start_time.strftime("%d %B %Y, %H:%M")
                end_time = list_pertandingan[i][2]
                end_time = end_time.strftime("%H:%M")

                tim_bertanding , err = query(f"select nama_tim from tim_pertandingan where id_pertandingan = '{list_pertandingan[i][0]}'")
                tim_bertanding = f"{tim_bertanding[0][0]} vs {tim_bertanding[1][0]}"
                for month in month_translations:
                    if month in start_time:
                        translated_month = month_translations[month]
                        start_time = re.sub(r'\b{}\b'.format(month), translated_month, start_time)

                print([start_time,end_time])
                
                info_pertandingan.append([tim_bertanding, stadium_name, start_time, end_time])

        context = {
        "info_pertandingan": info_pertandingan,
        "role": role
        }
    else:
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
                        

            end_time = list_pertandingan[i][2]
            end_time = end_time.strftime("%H:%M")

            info_pertandingan.append([tim_bertanding, stadium, start_time, end_time])
        context = {
        "info_pertandingan": info_pertandingan,
        "role": role
        }


    # if role == "MANAJER":
       

    
    return render(request, 'list_pertandingan.html', context)