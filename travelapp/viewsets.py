from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

# Create your views here.
class Modeviewset(viewsets.ModelViewSet):
    queryset=Mode.objects.all()
    serializer_class=ModeSerializer

class Routeviewset(viewsets.ModelViewSet):
    queryset=Route.objects.all()
    serializer_class=RouteSerializer

class Bookviewset(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
