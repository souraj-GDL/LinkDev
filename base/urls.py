from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('create-room/', views.createRoom, name='create_room'),
    path('update-room/<str:pk>/', views.updateRoom, name='update_room'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete_room'),
]