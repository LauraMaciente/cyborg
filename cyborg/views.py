from django.shortcuts import render


def index(request):
    return render (request,"cyborg/pages/index.html")

def produtos(request):
    return render (request,"cyborg/pages/products.html")