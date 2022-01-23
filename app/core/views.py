from re import search
from django.db import models
from django.db.models import query
from django.http import response
from django.shortcuts import render
from rest_framework import authentication
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets,filters
from core import serializers
from rest_framework.response import Response
from  core import models
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken, obtain_auth_token
from rest_framework.settings import api_settings
from core import permissions
from django.conf import settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly






# Create your views here.

class HelloApiView(APIView):
    '''test api view '''
    serializer_class = serializers.HelloSerializers

    def get(self,request,format=None):
        '''return a list of apiview features'''
        an_apiview = [
            'use HTTP method as functions (get ,post,patch,put,delete)',
            'is similar to teridinall django view',
            'gives you the more control over your application logic',
            'is mapped manually to url'
        ]
        return Response({'message':'hello','an_apiview':an_apiview})

    def post(self,request):
        '''create a hello msg with name'''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self ,request ,pk=None):
        '''handle update object'''
        return Response ({'method':'PUT'})

    def patch(self,request,pk=None):
        '''Handle a particular update of an object'''
        return Response({'method ':'PATCH'})

    def delete(self, request ,pk=None):
        '''Delete an object'''
        return Response({'method':'DELETE'})




class HelloViewSet(viewsets.ViewSet):
    '''TEST API VIEWSET'''
    serializer_class = serializers.HelloSerializers

    def list(self, request):
         '''return a hello message'''

         a_viewset = [
             'uses action (list,create,retrive,update,partially_update)',
             'automatically maps to urls using routers',
             'provide more funcnility with less code',
         ]

         return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self,request):
        '''create a hello msg with name'''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrive(self ,request ,pk=None):
        '''HANDLE GETTING AN OBJECTS WITH ITSA ID'''
        return Response ({'HTT Pmethod':'GET'})

    def update(self,request,pk=None):
        '''HANDLEUPDATING AN OBJECT'''
        return Response({'HTTPmethod ':'PUT'})

    def partial_update(self, request ,pk=None):
        '''HANDLE UPDATING PART OF AN OBJECT'''
        return Response({'method':'PATCH'})

    def destroy(self,request,pk=None):
        '''HANDLE REMOVING AN OBJECT'''
        return Response({'http_method':'DELETE'})

class UserProfileViewset(viewsets.ModelViewSet):
    '''handle creating ad updating profiles'''
    serializer_class=serializers.UserProfileSerializer
    queryset= models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email')


class UserLoginApiView(ObtainAuthToken):
    '''Handle creating user authentication token'''
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    '''handle creating ,reading and updating profile  feed item'''
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes =(
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly
    )

    def perform_create(self, serializer):
        '''sets the user profile to the logged in user'''
        serializer.save(user_profile=self.request.user)
        

