from django.contrib import admin
from .models import League, Team, Game, Player
# Register your models here.


admin.site.register(League)
admin.site.register(Team)

admin.site.register(Game)
admin.site.register(Player)


