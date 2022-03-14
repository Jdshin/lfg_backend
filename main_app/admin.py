from django.contrib import admin
from main_app.models import Player, Blacklist, Game, Event

class PlayerAdmin(admin.ModelAdmin):
    model = Player

admin.site.register(Player, PlayerAdmin)
admin.site.register(Game)
admin.site.register(Event)
admin.site.register(Blacklist)