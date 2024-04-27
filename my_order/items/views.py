from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Страница моего порядка")


def categories(request, catid):
    return HttpResponse(f"<h1> Категория {catid}</h1>")
