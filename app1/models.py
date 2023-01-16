from django.db import models

# Create your models here.
class Student (models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=3)
    roll_number=models.CharField(max_length=10)
    village=models.CharField(max_length=200)


