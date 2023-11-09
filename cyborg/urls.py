from django.urls import path
from . import views

app_name = "cyborg"

urlpatterns = [
    path("", views.index, name="index"),
    path("produtos/", views.produtos, name='produtos'),
]
