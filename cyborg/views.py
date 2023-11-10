from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Products


def index(request):
    return render (request,"cyborg/pages/index.html")

def produtos(request): 
    product_list = Products.objects.all()
    paginator = Paginator(product_list, 2)  # Mostra 10 produtos por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render (request,"cyborg/pages/products.html", {
        'page_obj': page_obj,
    })

 