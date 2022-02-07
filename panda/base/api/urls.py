from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('get-rooms', views.getRooms),
    path('rooms/<str:pk>/', views.getRoom),
]
