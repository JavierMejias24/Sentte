from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "senttevaluationapp/home.html")

def grupos(request):
    return render(request, "senttevaluationapp/grupos.html")

def graficos(request):
    return render(request, "senttevaluationapp/graficos.html")

def ayuda(request):
    return render(request, "senttevaluationapp/ayuda.html")

def ayuda(request):
    return render(request, "senttevaluationapp/login.html")