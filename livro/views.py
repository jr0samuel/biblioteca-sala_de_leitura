from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse("Mundo Mário da Leitura")

def sala(request):
    return HttpResponse("Sala de Leitura")