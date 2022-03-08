from ssl import _create_default_https_context
from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from main_app.models import Game, Event, Player


# Create your views here.
class Signup(View):
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/user/{}".format(user._id))
        else:
            context = {
                'status' : 400
            }
            return context
        
class Home(View):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO limit game object maybe for the future
        context["homeData"] =  Game.objects.all()
        return context
        