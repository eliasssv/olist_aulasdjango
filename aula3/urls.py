from django.urls import path
from .views import index, seta_cookie, redirect

app_name = "aula3"

urlpatterns = [
    path('', index),
    path('cookie', seta_cookie),
    path('uol', redirect),
] 
