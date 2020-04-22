from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'shop/index.html')


def about(requests):
    return HttpResponse("We are at about")


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
