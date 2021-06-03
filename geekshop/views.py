from django.shortcuts import render
from mainapp.models import ProductCategory, Product
import json


def index(request):
    title = 'Главная'
    products = Product.objects.all()[:4]

    content = {'title': title, 'products': products}
    return render(request, 'index.html', content)


def contacts(request):
    return render(request, 'contact.html')
