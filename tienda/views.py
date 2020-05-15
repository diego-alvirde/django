from django.http import HttpResponse
from django.shortcuts import render

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

def login(request):
    print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username,password)
    return render(request,'users/login.html', {

    }) 