from django.urls import path
from . import views

app_name = "cyborg"

urlpatterns = [
    path("", views.index, name="index"),
    path("produtos/", views.produtos, name='produtos'),
    path("sobre/", views.sobre, name='sobre'),  
    path("login/", views.login, name='login'), 
]
