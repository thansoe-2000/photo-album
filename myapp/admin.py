from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
     list_display = ['id', 'name', 'user']

     
class PhotoAdmin(SummernoteModelAdmin):
     list_display = ['id', 'category', 'image', 'title']
     summernote_fields = ('description')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)