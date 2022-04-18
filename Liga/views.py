from django.shortcuts import render
from django.http import HttpResponse
from .models import Player
from .forms import PlayerForm
# Create your views here.

def home_view(request, *args, **kwargs):
    
    my_context = {
        "datum" : "4.4.2022"
    }
    return render(request, "index.html", my_context)


def player_detail_view(request):
    
    player = Player.objects.get(id=1)
    

    context = {
        'player': player
    }
    return render(request, "player/detail.html", context)

def player_create_view(request):
    
    form = PlayerForm(request.POST or None)
    if form.is_valid():
        form.save()
    

    context = {
        'form': form
    }
    return render(request, "player/create.html", context)


