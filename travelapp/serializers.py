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
        fields=['mode','route','passengers','total_price','seat','message']
        read_only_fields=['total_price','message','confirmation']

class SeatSerializer(serializers.ModelSerializer):
    confirmation=serializers.ReadOnlyField()
    class Meta:
        model=Seat
        fields=['route','seat_no','confirmation']
        validators=[]

    def validate(self,data):
        seat_no=data.get('seat_no')
        route=data.get('route')
        mode=data.get('mode')

        qs=Seat.objects.filter(route=route,seat_no=seat_no)

        if (qs.exists()):
            raise serializers.ValidationError(
                f"Seat {seat_no} is not available"            )
        return data





