from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

class Game(models.Model):
    name = models.CharField(max_length=100)
    crossplay = models.BooleanField(default=False)
    img = ImageField(blank=True, manual_crop="32:10")
    
    def __str__(self):
        return self.name
        
    
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="player")
    accountName = models.CharField(max_length=100)
    games = models.ManyToManyField(Game, related_name="players", blank=True)
    
    def __str__(self):
        return self.accountName

class Event(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="events")
    name = models.CharField(max_length=100, default="{} Event".format(game.name))
    players = models.ManyToManyField(Player, related_name="events", blank=True)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    creator = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="created_events")
    spotsAvailable = models.IntegerField(default=0)
    spotsTotal = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name

class Blacklist(models.Model):
    user = models.OneToOneField(Player, on_delete=models.CASCADE, related_name="blacklist")
    blockedUsers = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="blockedPlayers")
    
    def __str__(self):
        return self.user.username
