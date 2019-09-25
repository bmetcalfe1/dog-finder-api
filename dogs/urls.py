from django.urls import path

from . import views

urlpatterns = [
    path('dogparks/', views.DogParkList.as_view()),
    path('dogs/', views.DogList.as_view()),
    path('dogrange', views.DogRange.as_view()),
    path('dogs/<int:pk>/', views.DogDetail.as_view()),
]
