from django.urls import path
from . import views

urlpatterns = [
    path('', views.film_list, name='film_list'),  # список фильмов по /
    path('add/', views.add_film, name='add_film'),
]