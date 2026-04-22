from .models import *
from rest_framework import serializers

class ModeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mode
        fields='__all__'

class ModeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ModeType
        fields=['modes','service','price_per_km'] 


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Route
        fields="__all__"

class BookSerializer(serializers.ModelSerializer):
    total_price=serializers.ReadOnlyField()
    message=serializers.ReadOnlyField()
    class Meta:
        model=Book
        fields=['mode','route','passengers','total_price','message']
        read_only_fields=['total_price','message']


