from django.contrib import admin
from main_app.models import Player, Blacklist, Game, Event

admin.site.register(Game)
admin.site.register(Event)
admin.site.register(Player)
admin.site.register(Blacklist)