from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
class ItemAPIVier(generics.ListAPIView):
    queryset = TheItem.objects.all()
    serializer_class = TheItemSerializer
def index(request):
    return HttpResponse("Страница моего порядка")


def categories(request, catid):
    return HttpResponse(f"<h1> Категория {catid}</h1>")
