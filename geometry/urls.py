from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>', views.get_rectangle_area, name='name-rectangle'),
    path('square/<int:side>/', views.get_square_area, name='name-square'),
    path('circle/<int:radius>/', views.get_circle_area, name='name-circle'),
    path('get_rectangle_area/<int:width>/<int:height>', views.get_rectangle_area),
    path('get_square_area/<int:side>/', views.get_square_area),
    path('get_circle_area/<int:radius>/', views.get_circle_area),
]