from django.contrib import admin
from.models import *

# Register your models here.
class Studenadmin(admin.ModelAdmin):
    list_display=['name','age','roll_number','village']

admin.site.register(Student,Studenadmin)
