from django.contrib import admin
from .models import  Singer,Song,Menu,Hotel


# Register your models here.
admin.site.register(Singer)
admin.site.register(Song)
admin.site.register(Menu)
admin.site.register(Hotel)

# @admin.register(Singer)
# class SingerAdmin(admin.ModelAdmin):
#     list_display = ['id','name','gender']

# @admin.register(Song)
# class SongAdmin(admin.ModelAdmin):
#     list_display = ['id','title','singer','duration']
