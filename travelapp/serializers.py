from .models import Route,Mode,Book
from rest_framework import serializers

class ModeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mode
        fields="__all__" 


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Route
        fields="__all__"

class BookSerializer(serializers.ModelSerializer):
    total_price=serializers.ReadOnlyField()
    class Meta:
        model=Book
        fields=['mode','route','passengers','total_price']
        read_only_fields=['total_price']


