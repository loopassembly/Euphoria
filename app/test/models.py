

from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,\
     AbstractBaseUser,PermissionsMixin

# from model_utils import Choices
# Create your models here.



class UserManager(BaseUserManager):
    
    
    def create_user(self,email,name,password=None):
        '''create new user profile'''
        if not email:
            raise ValueError('user must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email ,name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self ,email ,name ,password):
        '''create ans save a new superuser with given details'''
        user = self.create_user(email,name,password)
        user.is_superuser =True
        user.is_staff = True
        user.save(using=self._db)

        return user

class User( AbstractBaseUser,PermissionsMixin,models.Model):
    email = models.EmailField( max_length=254,unique=True)
    USERNAME_FIELD = 'email'
    name =  models.CharField( max_length=50)


    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

   
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''retrive full nae of user'''
        return self.name

    def get_short_name(self):
        '''retrive short name of user'''
        return self.name

    def __str__(self):
        '''return string representation of user'''
        return self.email

    # @property
    # def items(self):
    #     return self.items_set.all()



class Menu(models.Model):
    STATUS =(
       ('available', 'Available'),
       ('unavailable', 'Unavailable')
       )

    FOOD_TYPE=(
        ('veg','VEG'),
        ('non-veg','NON-VEG'),
        ('drinks','DRINKS'),
        ('sweets','SWEETS')

    )
   

    menu =models.ForeignKey(User, on_delete=models.CASCADE,related_name='items')
    item_name = models.CharField( max_length=50)
    item_image = models.ImageField(upload_to="menu-images", height_field=None, width_field=None, max_length=None,null=True,blank=True)
    cost =models.IntegerField()
    bake_time =models.CharField( max_length=50)
    status=models.CharField(max_length=50,choices=STATUS)
    food_type=models.CharField(max_length=50,choices=FOOD_TYPE)

    def __str__(self):
      return self.item_name