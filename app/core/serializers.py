from rest_framework import serializers

class HelloSerializers(serializers.Serializer):
    '''serializes a name field for  testiong our APIView'''
    name= serializers.CharField(max_length =10 )
