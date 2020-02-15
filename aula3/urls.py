from django.urls import path
from . import views 

app_name = "aula3"

urlpatterns = [
    path('', views.index),
    path('cookie', views.seta_cookie),
    path('uol', views.redirect),
    path('<int:code>', views.show_code),
    path('cat/<int:code>', views.show_cat),
    path('get/', views.show_get_values),
    path('post/', views.show_post_values),
] 
