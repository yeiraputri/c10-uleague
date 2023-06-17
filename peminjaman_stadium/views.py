from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from utils.query import query
from django.contrib import messages

# Create your views here.
@csrf_exempt
def peminjaman_stadium(request):
    role = request.COOKIES.get('role')
    id_manajer = request.COOKIES.get('userId')
    is_available = request.COOKIES.get('insert_peminjaman')
    # masalahnya tinggal ngeclear cookie is_available

    if role == None:
        return redirect('home:login')
    if role != "MANAJER":
        return redirect('home:home')
    
    if is_available == None:
        pass
    elif is_available == "1":
        messages.success(request, 'Stadium berhasil dipinjam')
    else: 
        messages.error(request, is_available)

    list_peminjaman, err = query(f"select s.nama, concat(p.start_datetime, ' - ', p.end_datetime) as waktu from peminjaman as p, stadium as s where p.id_stadium = s.id_stadium and p.id_manajer = '{id_manajer}'")
    context = {
        "role": role,
        "list_peminjaman": list_peminjaman
    }
    response = render(request, 'peminjaman_stadium.html', {}) 
    response.set_cookie('insert_peminjaman', None)

    # Update peminjaman
    if request.method == 'POST':
        response = render(request, 'update_peminjaman.html', {}) 
        data = request.POST.get('data')
        data = data.split("|")
        nama_stadium_update = data[0]
        date_update = data[1]
        date_update = date_update.split(" - ")
        date_update = date_update[0]
        response.set_cookie('nama_stadium_update', nama_stadium_update)
        response.set_cookie('date_update', date_update)
        return response
    
    return render(request, 'peminjaman_stadium.html', context)

@csrf_exempt
def pilih_stadium(request):
    role = request.COOKIES.get('role')
    if role == None:
        return redirect('home:login')
    if role != "MANAJER":
        return redirect('home:home')

    list_stadium, err = query("select id_stadium, nama from stadium")
    context = {
        "role": role,
        "list_stadium": list_stadium
    }

    if request.method == 'POST':
        id_stadium = request.POST.get('id_stadium')
        date = request.POST.get('date')
        if id_stadium != None and date != None:
            response = redirect('peminjaman_stadium:peminjaman_stadium')
            response.set_cookie('insert_peminjaman', '1')
            insert_peminjaman, err = query(f"insert into peminjaman (id_stadium, id_manajer, start_datetime, end_datetime) values ('{id_stadium}', '{request.COOKIES.get('userId')}', '{date} 00:00:00', '{date} 23:59:59')")
            err = str(err).split("\n")[0]
            response.set_cookie('insert_peminjaman', err)
            return response
    return render(request, 'pilih_stadium.html', context)

@csrf_exempt
def update_peminjaman(request):
    role = request.COOKIES.get('role')
    nama_stadium_update = request.COOKIES.get('nama_stadium_update')
    date_update = request.COOKIES.get('date_update')

    if role == None:
        return redirect('home:login')
    if role != "MANAJER":
        return redirect('home:home')
    
    if request.method == 'POST':
        response = redirect('peminjaman_stadium:peminjaman_stadium')
        date = request.POST.get('date')
        response.set_cookie('insert_peminjaman', '1')
        try: 
            update_peminjaman_obj, err= query(f"update peminjaman set start_datetime = '{date} 00:00:00', end_datetime = '{date} 23:59:59' where id_manajer = '{request.COOKIES.get('userId')}' and id_stadium = (select id_stadium from stadium where nama = '{nama_stadium_update}') and start_datetime = '{date_update}'")
        except Exception as e:
            response.set_cookie('insert_peminjaman', e)
        return response
    
    context = {
        "role": role,
        "nama_stadium_update": nama_stadium_update,
        "date_update": date_update,
    }
    
    return render(request, 'update_peminjaman.html', context)
    

        




# def list_waktu_stadium(request):
#     role = request.COOKIES.get('role')
#     id_stadium = request.COOKIES.get('id_stadium')
#     date = request.COOKIES.get('date')

#     nama_stadium, err = query(f"select nama from stadium where id_stadium = '{id_stadium}'")

#     if role == None:
#         return redirect('home:login')
#     if role != "MANAJER":
#         return redirect('home:home')
    
#     # ambil data dari post terus masukan ke html
    
#     # nama_stadium, err = query(f"select nama from stadium where id_stadium = '{id_stadium}'")


#     context = {
#         "role": role,
#         "nama_stadium": nama_stadium[0][0],
#         "date": date,
#     }

#     return render(request, 'list_waktu_stadium.html', context)
