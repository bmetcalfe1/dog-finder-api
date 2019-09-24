from rest_framework import serializers
from . import models


class DogSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'breed', 'latitude', 'longitude', 'created_at', 'updated_at',)
        model = models.Dog


class DogParkSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'latitude', 'longitude', 'created_at', 'updated_at',)
        model = models.DogPark
