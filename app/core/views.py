from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from core import serializers




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
         