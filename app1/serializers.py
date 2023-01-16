from .models import *
from rest_framework import serializers

class Studentserializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    age=serializers.CharField(max_length=3)
    roll_number=serializers.CharField(max_length=10)
    village=serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
        