from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SingerSerializer,SongSerializer,MenuSerializer,HotelSerializer
from .models import Hotel, Menu, Singer,Song


class SingerViewSet(viewsets.ModelViewSet):
   queryset = Singer.objects.all()
   serializer_class = SingerSerializer


class SongViewSet(viewsets.ModelViewSet):
   queryset = Song.objects.all()
   serializer_class = SongSerializer

class MenuViewSet(viewsets.ModelViewSet):
   queryset = Menu.objects.all()
   serializer_class = MenuSerializer

class HotelViewSet(viewsets.ModelViewSet):
   queryset = Hotel.objects.all()
   serializer_class = HotelSerializer