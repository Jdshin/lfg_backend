import json
from ssl import _create_default_https_context
from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.views.generic import TemplateView
from main_app.models import Game, Event, Player
from django.http import JsonResponse
from django.core import serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer

# Create your views here.
class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        res = {
            'form' : form
        }
        return JsonResponse(res)
        
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/user/{}".format(user._id))
        else:
            res = {
                'status' : 400
            }
            return JsonResponse(res)
        
class Home(TemplateView):
    def get(self, request):
        return render(request, 'home.html')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO limit game object maybe for the future
        context["homeData"] =  Game.objects.all()
        return context
    
class Games(View):
    def get(self, request, **kwargs):
        # TODO Possibly need to convert to async call for hosting
        games = Game.objects.all()
        json_response = {}
        
        # TODO Figure out image sending logic
        for game in games:
            json_str = json.dumps(
                {
                    'name' : game.name,
                    'crossplay' : game.crossplay,
                    'img' : "https://ucarecdn.com/{}/".format(game.img.uuid)
                }
            )
            json_response["{}".format(game.name)] = json_str
        return JsonResponse(json_response)
    
class Events(View):
    def get(self, request, **kwargs):
        
        events = Event.objects.all()
        json_response = {}

        for event in events:
            
            players = event.players.all()
            
            attendees = [player.accountName for player in players]
            
            json_str = json.dumps(
                {
                    'pk': event.pk,
                    'game': event.game.name,
                    'name': event.name,
                    'desc': event.description,
                    'location': event.location,
                    'spots': event.spotsAvailable,
                    'creator': event.creator.accountName,
                    'players': attendees,
                }
            )
            json_response["{}".format(event.id)] = json_str
        return JsonResponse(json_response)
        
class UserCreate(APIView):
    permissions_classes = (permissions.AllowAny,)
    
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
