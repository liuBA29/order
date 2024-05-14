from rest_framework import serializers
from .models import *

class TheItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=TheItem
        fields = ('name', 'location', 'is_actual')