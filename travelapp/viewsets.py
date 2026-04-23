from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

# Create your views here.
class Modeviewset(viewsets.ModelViewSet):
    queryset=Mode.objects.all()
    serializer_class=ModeSerializer
class ModeTypeviewset (viewsets.ModelViewSet):
    queryset=ModeType.objects.all()
    serializer_class=ModeTypeSerializer

class Routeviewset(viewsets.ModelViewSet):
    queryset=Route.objects.all()
    serializer_class=RouteSerializer

class Bookviewset(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class Seatviewset(viewsets.ModelViewSet):
    queryset=Seat.objects.all()
    serializer_class=SeatSerializer