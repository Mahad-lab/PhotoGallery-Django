from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('add', views.addPhoto, name='add'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
]
