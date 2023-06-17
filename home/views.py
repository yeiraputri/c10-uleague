from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from utils.query import query
import uuid

# Create your views here.
# @login_required(login_url='/login_register/')
def home(request):
    role = request.COOKIES.get("role")

    context = {
        'role': role
    }
    return render(request, 'home.html', context)


@csrf_exempt
def login_register(request):
    return render(request, 'login_register.html')

def register(request):
   
    return render(request, 'register.html')

def register_manajer(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        nama_depan = request.POST.get("nama_depan")
        nama_belakang = request.POST.get("nama_belakang")
        nomor_hp = request.POST.get("telp")
        email = request.POST.get("email")
        alamat = request.POST.get("alamat")
        role = request.POST.get("role")
        id = str(uuid.uuid4())

        print([username, password, nama_depan, nama_belakang, nomor_hp, email, alamat, role, id])
        
        
        ins_user_system, err1 = query(f"insert into user_system(username,password) values ('{username}', '{password}')")
        if err1 != None:
            e = str(err1).split('\n')[0]
            print(e)
            context = {
                "role": role,
                "messages": e,
            }
            return render(request, 'register_manajer.html', context)

        
        ins_non_pemain, err = query(f"insert into non_pemain(id,nama_depan,nama_belakang,nomor_hp,email,alamat) values ('{id}', '{nama_depan}', '{nama_belakang}','{nomor_hp}', '{email}','{alamat}')")
        ins_status_non_pemain, err = query(f"insert into status_non_pemain(id_non_pemain,status) values ('{id}', '{role}')")
        ins_manajer, err = query(f"insert into manajer(id_manajer ,username) values ('{id}', '{username}')")

        
       

        messages.success(request, "Berhasil mendaftar sebagai manajer!")
        return redirect("home:login")
            
        

    return render(request, "register_manajer.html")

def register_penonton(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        nama_depan = request.POST.get("nama_depan")
        nama_belakang = request.POST.get("nama_belakang")
        nomor_hp = request.POST.get("telp")
        email = request.POST.get("email")
        alamat = request.POST.get("alamat")
        role = request.POST.get("role")
        id = str(uuid.uuid4())

        print([username, password, nama_depan, nama_belakang, nomor_hp, email, alamat, role, id])
        
        try:
            ins_user_system, err = query(f"insert into user_system(username,password) values ('{username}', '{password}')")
            ins_non_pemain, err = query(f"insert into non_pemain(id,nama_depan,nama_belakang,nomor_hp,email,alamat) values ('{id}', '{nama_depan}', '{nama_belakang}','{nomor_hp}', '{email}','{alamat}')")
            ins_status_non_pemain, err = query(f"insert into status_non_pemain(id_non_pemain,status) values ('{id}', '{role}')")
            ins_penonton, err = query(f"insert into penonton(id_penonton ,username) values ('{id}', '{username}')")
        
            messages.success(request, "Berhasil mendaftar sebagai penonton!")
            return redirect("home:login")
            
        except Exception as e:
            messages.error(request, e)
            
    return render(request, "register_penonton.html")

def register_panitia(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        nama_depan = request.POST.get("nama_depan")
        nama_belakang = request.POST.get("nama_belakang")
        nomor_hp = request.POST.get("telp")
        email = request.POST.get("email")
        alamat = request.POST.get("alamat")
        role = request.POST.get("role")
        id = str(uuid.uuid4())
        jabatan = request.POST.get("jabatan")
        print([username, password, nama_depan, nama_belakang, nomor_hp, email, alamat, role, id, jabatan])
        
        try:
            ins_user_system, err = query(f"insert into user_system(username,password) values ('{username}', '{password}')")
            ins_non_pemain, err = query(f"insert into non_pemain(id,nama_depan,nama_belakang,nomor_hp,email,alamat) values ('{id}', '{nama_depan}', '{nama_belakang}','{nomor_hp}', '{email}','{alamat}')")
            ins_status_non_pemain, err = query(f"insert into status_non_pemain(id_non_pemain,status) values ('{id}', '{role}')")

            q4 =f"insert into panitia(id_panitia, jabatan ,username) values ('{id}', '{jabatan}', '{username}')"
            ins_panitia, err = query(q4)
            print(q4)

            messages.success(request, "Berhasil mendaftar sebagai panitia!")
            return redirect("home:login")
            
        except Exception as e:
            messages.error(request, e)
            
    return render(request, "register_panitia.html")




@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_id = None

       
       
        get_user = query(f"select * from user_system where username = '{username}' and password = '{password}'")
        # print(len(get_user[0]) == 0)
        # print(get_user)
        # print(get_user[0][0][0])


        if len(get_user[0]) != 0:
            role = None

            #Check manajer
            get_role = query(f"select * from manajer where username = '{username}'")
            # print(get_role)
            role = "MANAJER"
            
            

            if len(get_role[0]) == 0:

                #Check panitia
                get_role = query(f"select * from panitia where username = '{username}'")
                role = "PANITIA"
                if len(get_role[0]) == 0:

                    #Check penonton
                    get_role = query(f"select * from penonton where username = '{username}'")
                    role  = "PENONTON"   

                     
            
            user_id = get_role[0][0][0]
            print(user_id)
            context = {
                'username': username,
                'password': password,
                'role': role,
            }
            
            
            # print(role)
            response = render(request, 'home.html', context)
            response.set_cookie('role', role)
            response.set_cookie('username', username)
            response.set_cookie('userId', user_id)
            return response
            
        else:
            context = {
                'message': 'Cek kembali username dan password anda!',
                'status': 'error',
                'role': None,
            }
            return render(request, 'login1.html', context)

        
    context = {}
    return render(request, 'login1.html', context)

def logout_user(request):
    response = redirect(reverse('home:login'))
    for cookie in request.COOKIES:
        response.delete_cookie(cookie)
    return response

