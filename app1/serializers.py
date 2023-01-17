from .models import *
from rest_framework import serializers

class Studentserializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    age=serializers.CharField(max_length=3)
    roll_number=serializers.CharField(max_length=10)
    village=serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.age=validated_data.get('age',instance.age)
        instance.roll_number=validated_data.get('roll_number',instance.roll_number)
        instance.village=validated_data.get('village',instance.village)
        instance.save()
        return instance        