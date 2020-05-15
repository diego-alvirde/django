from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html", {
        'message':'Diego',
        'anio':2020
    })