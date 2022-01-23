from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from .models import Hotel, Menu, Singer,Song




class SongSerializer(serializers.ModelSerializer):
   class Meta:
       model = Song
       fields = ('id', 'title', 'Singer')

class SingerSerializer(serializers.ModelSerializer):
    # species1 = SongSerializer(many=True)
    sungby = SongSerializer(many=True)
    class Meta:
        model = Singer
        fields = ('id', 'name', 'gender' )


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','name','cost','time','menu']


class HotelSerializer(serializers.ModelSerializer):
    items = MenuSerializer(many=True)
    class Meta:
        model=Hotel
        fields= '__all__'


 

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        hotel =Hotel.objects.create(**validated_data)
        
        Menu.objects.create(menu=hotel, **items_data)
        return hotel
