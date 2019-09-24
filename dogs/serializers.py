from rest_framework import serializers
from . import models


class DogSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'breed', 'created_at', 'updated_at',)
        model = models.Dog
