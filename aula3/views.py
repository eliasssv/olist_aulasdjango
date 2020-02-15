from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

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

def show_code(request, code):
    html = f"<h1>O código é {code}</h1>"
    response = HttpResponse(html)
    return response

def show_cat(request, code):
    return HttpResponseRedirect(f"https://http.cat/{code}")

def show_get_values(request):
    nome = request.GET.get("nome", "Não informado")
    html = f"<h1>Bem vindo {nome}</h1>"
    return HttpResponse(html)

@csrf_exempt
def show_post_values(request):
    head =""
    if request.method=="POST":
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        head = f"<h1>Bem vindo {nome} {sobrenome}</h1>"

    html = """
        <form method=POST>
            <label for="fname">Nome:</label><br>
            <input type="text" id="nome" name="nome" value=""><br>
            <label for="sobrenome">Sobrenome:</label><br>
            <input type="text" id="sobrenome" name="sobrenome" value=""><br><br>
            <input type="submit" value="salvar">
         </form> 
    """
    return HttpResponse(head+html)
