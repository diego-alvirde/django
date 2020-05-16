from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages

def index(request):
    return render(request,"index.html", {
        'message':'Listado de Productos',
        'titulo':'Productos',
        'products': [
            {'title':'Playera','price':5,'stock':True},
            {'title':'Camisa','price':7,'stock':True},
            {'title':'Mochila','price':20,'stock':False}
        ]
    })

def login_view(request):
    print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            login(request,user)            
            messages.success(request,'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request,'Usuario o contraseña no validos')           

    return render(request,'users/login.html', {

    })

def logout_view(request):
    logout(request)
    messages.success(request,'Sesión cerrada exitosamente')
    return redirect('login')

