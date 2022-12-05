from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='horoscope-index'),
    path('<str:type>/', views.get_elements),
    path('type/<str:types_zodiac>', views.get_sign_of_elements, name='element-name'),
    path('<int:sign_of_zodiac>', views.get_horoscope_by_sign_by_number),
    path('<str:sign_of_zodiac>', views.get_horoscope_by_sign, name="horoscope-name"),
]

