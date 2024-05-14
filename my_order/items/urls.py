from django.urls import path
from .views import *



urlpatterns = [
    path('', index, name="home"),
    path('category/<int:catid>/', categories),
    path('api/v1/allitems/', ItemAPIVier.as_view()),
]