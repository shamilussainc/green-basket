from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return render(request=request, template_name="frontend/index.html", context=None)

def shop(request):
    return render(request=request, template_name="frontend/shop.html", context=None)

def shop(request):
    return render(request=render, template_name="frontend/shop-detail.html", context=None)