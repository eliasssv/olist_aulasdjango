from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "alunos": [
            "joao",
            "maria",
            "jose",
        ]
    }
    return render(request, "aula4/index.html", context = context)