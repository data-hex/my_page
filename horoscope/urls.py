from django.urls import path
from . import views

urlpatterns = [
    path('<int:sign_of_zodiac>/', views.get_horoscope_by_sign_by_number),
    path('<str:sign_of_zodiac>/', views.get_horoscope_by_sign),
]

