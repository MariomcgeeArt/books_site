from django.contrib import admin
from django.urls import include, path
from . import views



urlpatterns = [
    # ex: /polls/
    path('', views.home, name='home'),
    path('book/<int:book_id>/', views.detail),
   
]