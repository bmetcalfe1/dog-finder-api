from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from . import models
from . import serializers


class DogList(generics.ListCreateAPIView):
    queryset = models.Dog.objects.all()
    serializer_class = serializers.DogSerializer

    def post(self, request):
        serializer = serializers.DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # serializer.save(creator=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Dog.objects.all()
    serializer_class = serializers.DogSerializer
