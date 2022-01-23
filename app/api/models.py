from django.db import models



# Create your models here.


class  Singer(models.Model):
   
   name = models.CharField( max_length=100)
   password=models.CharField( max_length=50,verbose_name='password',default='admin@123')
   gender = models.CharField( max_length=10)

   def __str__(self):
      return self.name

class Song(models.Model):
   title = models.CharField( max_length=100)
   Singer = models.ForeignKey(Singer,on_delete=models.CASCADE,related_name='sungby')

   def __str__(self):
      return self.title




# class Credentials(models.Model):
   
#    name=models.CharField( max_length=200)
#    email=models.EmailField(max_length=200)
#    password=models.CharField( max_length=200)
   # password = models.




class Hotel(models.Model):
   name=models.CharField(max_length=50)
   email=models.EmailField(max_length=200)
   password=models.CharField( max_length=200)
   
   def __str__(self):
      return self.name
   
class Menu(models.Model):
   name=models.CharField( max_length=200)
   # image=models.ImageField(null=True)
   cost=models.IntegerField()
   time = models.CharField(max_length=50)
   menu = models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='items')

   def __str__(self):
      return self.name