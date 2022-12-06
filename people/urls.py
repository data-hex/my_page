from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_people),
    path('beautiful_table', views.get_beautiful)
]