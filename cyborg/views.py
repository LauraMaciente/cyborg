from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from .models import Products
from django.contrib.auth import authenticate, login as auth_login


def index(request): 
    page_name = "Home"
    return render(request, "cyborg/pages/index.html", {
        'page_name': page_name, 
    })

def produtos(request): 
    product_list = Products.objects.all()
    paginator = Paginator(product_list, 10)

    page_number = request.GET.get('page')
    products_paginator = paginator.get_page(page_number)

    return render(request, "cyborg/pages/products.html", {
        'products_paginator': products_paginator,
        'page_name': "Produtos",
    })
    
    
def sobre(request):
    return render(request, "cyborg/pages/contact.html",{
        'page_name': "Contato",
    })

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('cyborg:index')
        else:
            # Uma mensagem de erro pode ser adicionada aqui
            pass

    page_name = "Login"
    return render(request, "cyborg/pages/login.html", {'page_name': page_name})

