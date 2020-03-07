from django.shortcuts import render
from .forms import UserLoginForm
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse

def index(request):
    next = request.GET.get("next", reverse("login"))
    form = UserLoginForm()
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            next = request.POST.get("next", reverse("login"))
            return HttpResponseRedirect(next)

    context = {
        "form": form,
        "next": next,
    }
    return render(request, 'aula7/index7.html', context=context)

@login_required
def restrita(request):
    return HttpResponse("View Restrita")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

@permission_required('aula5.view_carrinho')
def permission_view(request):
    return HttpResponse("view com permissao")