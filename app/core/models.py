from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AnonymousUser,BaseUserManager,\
    PermissionsMixin, User, UserManager
from django.db.models.fields import EmailField

# Create your models here.
class UserProfileManager(BaseUserManager):
    '''manager for user profiles'''
    
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

class Modules(models.Model):
    module_name = models.CharField(max_length=50)
    module_duaration = models.IntegerField()
    class_room = models.IntegerField()

    def __str__(self):
        return self.module_name

class UserProfile(AbstractBaseUser , PermissionsMixin ,models.Model):
    '''Database model for users in the system'''
    email = models.EmailField( max_length=254,unique=True)
    USERNAME_FIELD = 'email'
    name =  models.CharField( max_length=50)
    modules = models.ManyToManyField(Modules)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

   
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



    
class ProfileFeedItem(models.Model):
     '''Profile  status Update'''
     user_profile = models.ForeignKey(
          settings.AUTH_USER_MODEL,
          on_delete=models.CASCADE
     )
     status_text = models.CharField( max_length=255)
     created_on = models.DateTimeField(auto_now_add = True)

     def __str__(self):
         '''return the model as string'''
         return self.status_text