from django.shortcuts import render
from .models import Funcionario
from django.shortcuts import render

def lista_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, "funcionarios/lista.html", {"funcionarios": funcionarios})

def home(request):
    return render(request, "home.html")