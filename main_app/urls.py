from django.urls import path, include
from django.contrib import admin
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('user/<int:pk>', views.Signup.as_view(), name="signup"),
    path('games/', views.Games.as_view(), name="games"), 
    path('events/', views.Events.as_view(), name="events"),
    path('events/<int:pk>', views.Events.as_view(), name="event"),
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create/', views.UserCreate.as_view(), name="create_user")
]