from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range':range(1,nSlides),'product': products}
    return render(request, 'shop/index.html',params)


def about(request):
    return render(request, 'shop/about.html')


def contact(requests):
    return HttpResponse("We are at contacts")


def tracker(requests):
    return HttpResponse("We are at tracker")


def search(requests):
    return HttpResponse("We are at search")


def productView(requests):
    return HttpResponse("We are at product view")


def checkout(requests):
    return HttpResponse("We are at checkout")
