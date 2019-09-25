from django.db.models import F
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from . import models
from . import serializers


class DogParkList(generics.ListCreateAPIView):
    queryset = models.DogPark.objects.all()
    serializer_class = serializers.DogParkSerializer

    def post(self, request):
        serializer = serializers.DogParkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # serializer.save(creator=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class DogRange(generics.ListAPIView):
    serializer_class = serializers.DogSerializer

    def get(self, request):
        req_latitude = request.GET.get('latitude')
        req_longitude = request.GET.get('longitude')
        req_radius_km = int(request.GET.get('radius', 10))
        queryset = models.Dog.objects.annotate(
            radius_sqr=pow(F('latitude') - req_latitude, 2) + pow(F('longitude') - req_longitude, 2)
        ).filter(
            radius_sqr__lte=pow(req_radius_km / 9, 2)
        )
        return Response(list(queryset.values()), status=status.HTTP_200_OK)


class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Dog.objects.all()
    serializer_class = serializers.DogSerializer
