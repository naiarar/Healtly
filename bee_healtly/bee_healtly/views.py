from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    sexo = 'f'
    nome = 'Pedro'

    return render(request, 'index.html', {'sexo': sexo,'nome': nome})
