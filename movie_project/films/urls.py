from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_film, name='add_film'),
    path('films/', views.film_list, name='film_list'),
]