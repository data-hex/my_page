from django.urls import path
from . import views

urlpatterns = [
    path('<int:days>/', views.get_week_days_by_number),
    path('<str:days>/', views.get_week_days, name="week_days_name"),
]
