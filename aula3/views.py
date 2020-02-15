from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.utils import timezone

def index(request):
    html = "<h1>Bem vindo</h1>"
    response = HttpResponse(html)
    response['ultimo_acesso'] = timezone.now()
    return response

def seta_cookie(request):
    response = HttpResponse()
    response.set_cookie("my_name", value = 'Elias')
    return response

def redirect(request):
    return HttpResponseRedirect("http://uol.com.br")
    