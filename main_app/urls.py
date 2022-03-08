from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('user/<int:pk>', views.Signup.as_view(), name="signup"),
    path('games', views.Games.as_view(), name="games")
]