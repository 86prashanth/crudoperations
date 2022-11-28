from django.contrib import admin
from django.utils.html import format_html
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def photo(self,object):
        return format_html("<img src='{}' width:'48' height='48' style='border-radius:48px'/>".format(object.image.url))
    list_display=['id','name','email','password','photo']