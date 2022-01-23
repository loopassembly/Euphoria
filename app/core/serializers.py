from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers

from core import models


class ModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modules
        fields = ['id', 'module_name', 'module_duration', 'class_room']


class HelloSerializers(serializers.Serializer):
    '''serializes a name field for  testiong our APIView'''
    name= serializers.CharField(max_length =10 )

class UserProfileSerializer(serializers.ModelSerializer):
    '''serializers a user profile object'''

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_Kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

    def create(self, validated_data):
        '''create and return a new user'''
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name=validated_data['name'],
            password = validated_data['password']

        )
        # user2 = models.UserProfile.objects.create_user(
        #     email = validated_data['email'],
        #     name=validated_data['name'],
        #     password = validated_data['password']

        # )
        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    '''serializer profile feed items'''

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id' ,'user_profile' ,'status_text' ,'created_on')
        extra_kwargs = {
            'user_profile':{'read_only':True }
        }
