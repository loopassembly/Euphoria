
from pyexpat import model
from django.http import response
from rest_framework import serializers
from rest_framework.response import Response
from django.http import request

from .models import User,Menu

class MenuSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
       model = Menu
       fields = ("id","item_name","item_image","cost","bake_time","status",'food_type',"menu")
       extra_kwargs = {
            'item_name': {'validators': []},
        }
       read_only_fields = ('menu',)

class UserSerializer(serializers.ModelSerializer):
    items = MenuSerializer(many=True)
    
    class Meta:
        model = User
        fields = ("id","email","name","password",'items')
    #    extra_Kwargs = {
    #         'password':{
    #             'write_only': True,
    #             'style':{'input_type':'password'}
    #         }
    #    }
        extra_kwargs = {'password':
             {'write_only':True,
                'style':{'input_type':'password'}
                }
            }
        
    
    def create(self, validated_data):
        '''create and return a new user'''
        items_data = validated_data.pop('items')
        # menu =User.objects.create(**validated_data)
        menu = User.objects.create_user(
            email = validated_data['email'],
            name=validated_data['name'],
            password = validated_data['password']

        )
        
        for item in items_data:
            Menu.objects.create(**item,menu=menu)

      
        
        
    
        return menu

    def update(self, instance, validated_data):
       
        items = validated_data.pop('items')
        print(items)
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        res=False
        keep_items = []
        for choice in items:
            
            val_data_len=len(choice)
            
            if "id" in choice.keys():
                # print("id")
                if Menu.objects.filter(id=choice["id"]).exists():
                    c = Menu.objects.get(id=choice["id"])
                    c.item_name = choice.get('item_name', c.cost)
                    c.cost = choice.get('cost', c.item_name)
                    c.bake_time = choice.get('bake_time', c.bake_time)
                    c.status = choice.get('status', c.status)

                    c.save()
                    keep_items.append(c.id)
                else:
                    continue
            else:
                # model_val=Menu.objects.values_list('item_name',"menu")
                # user_val=choice["item_name"]
                # print(user_val)
                # print(model_val)
                # test =items
                # print(test)
                # if user_val not in  model_val:
                if not  Menu.objects.filter(item_name=choice['item_name'], menu=instance).exists():

                    c = Menu.objects.create(**choice, menu=instance)
                    keep_items.append(c.id) 
                    
                            
                else:
                    # print(Menu.objects.filter(id="").exists())
                    raise serializers.ValidationError("item with this name already exists")
                    
                    
 
       
        
             
            if "id" in choice.keys() and val_data_len==1:
                    print("id")
                    if Menu.objects.filter(id=choice["id"]).exists():
                        print(Menu.objects.filter(id=choice["id"]),"data")
                        c = Menu.objects.get(id=choice["id"])
                        print(c.id)
                        for i in Menu.objects.all():
                            
                            if i.id==c.id:
                                
                                i.delete()

        return instance
    
    


    # def get_dump_object(self, obj):
    #     mapped_object = {
    #         'id': obj.id
            
    #     }
    #     print(mapped_object)
    #     print("hi")

    #     return mapped_object