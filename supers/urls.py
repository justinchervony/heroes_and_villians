from django.urls import path
from . import views

urlpatterns = [
    path('', views.supers_list),
    path('<int:pk>', views.super_detail),
    path('heros_and_villains', views.heroes_and_villains),
]