from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.CharField(max_length=100)
    crossplay = models.BooleanField(default=False)
    
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="player")
    accountName = models.CharField(max_length=100)
    games = models.ManyToManyField(Game, related_name="players")

class Event(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="events")
    players = models.ManyToManyField(Player, related_name="events", blank=True)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    creator = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="created_events")
    spotsAvailable = models.IntegerField(default=0)

class BlockedPlayer(models.Model):
    blockedUser = models.OneToOneField(Player, on_delete=models.CASCADE, related_name="blocked_by")
    blockingUsers = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="blocking_players")
