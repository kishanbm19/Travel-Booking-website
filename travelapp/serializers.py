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
    class Meta:
        model=Book
        fields="__all__"


