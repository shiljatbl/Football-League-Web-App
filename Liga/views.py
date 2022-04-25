from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Player
from .forms import PlayerForm
# Create your views here.

def home_view(request, *args, **kwargs):
    
    my_context = {
        "datum" : "4.4.2022"
    }
    return render(request, "index.html", my_context)


def player_detail_view(request, id):
    
    #player = Player.objects.get(id=my_id)
    player = get_object_or_404(Player,id=id)

    context = {
        'player': player
    }
    return render(request, "player/detail.html", context)

def player_create_view(request):
    
    form = PlayerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PlayerForm()

    context = {
        'form': form
    }
    return render(request, "player/create.html", context)

def player_update_view(request, id=id):
    obj = get_object_or_404(Player, id=id)
    form = PlayerForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "player/create.html", context)


def player_list_view(request):
    queryset = Player.objects.all()
    context = {
        "object_list" : queryset
    }

    return render(request, "player/list.html", context)

def register(request):
    #queryset = Player.objects.all()
    context = {
        
    }

    return render(request, "register.html", context)

def login(request):
    #queryset = Player.objects.all()
    context = {
        
    }

    return render(request, "login.html", context)