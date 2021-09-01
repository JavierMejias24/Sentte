from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "home.html")

def grupos(request):
    return render(request, "grupos.html")

def graficos(request):
    return render(request, "graficos.html")

def ayuda(request):
    return render(request, "ayuda.html")

def login(request):
    return render(request, "login.html")

def index(request):
    return render(request, "index.html")