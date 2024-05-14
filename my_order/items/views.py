from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from .models import *
from .serializers import *

# Create your views here.

menu = ["Furniture", "Items", "Search"]

class ItemAPIVier(APIView):
    def get(self, request):

        items = TheItem.objects.all().values()
        # serializer_class = TheItemSerializer
        return Response({"items": list(items)})

    def post(self, request):
        item_new= TheItem.objects.create(
            name = request.data['name'],
            location_id = request.data['location_id'],

        )
        return Response({"item": model_to_dict(item_new)})

def index(request):
    items = TheItem.objects.all()
    return render(request, 'items/index.html', {'menu': menu, 'items':items })


def categories(request, catid):
    return HttpResponse(f"<h1> Категория {catid}</h1>")
