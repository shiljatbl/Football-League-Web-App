from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Player, Team, League, Game
from .forms import NewUserForm, PlayerForm, LoginForm, TeamForm, LeagueForm, GameForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
@login_required(login_url="/login")
def home_view(request, *args, **kwargs):
    
    my_context = {
        "datum" : "4.4.2022"
    }
    return render(request, "home/index.html", my_context)

@login_required(login_url="/login")
def player_detail_view(request, id):
    
    #player = Player.objects.get(id=my_id)
    player = get_object_or_404(Player,id=id)

    context = {
        'player': player
    }
    return render(request, "player/detail.html", context)
@login_required(login_url="/login")
def player_create_view(request):
    
    form = PlayerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PlayerForm()

    context = {
        'form': form
    }
    return render(request, "player/create.html", context)
@login_required(login_url="/login")
def player_update_view(request, id=id):
    obj = get_object_or_404(Player, id=id)
    form = PlayerForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "player/create.html", context)

@login_required(login_url="/login")
def player_list_view(request):
    queryset = Player.objects.all()
    context = {
        "object_list" : queryset
    }

    return render(request, "player/list.html", context)

def register(request):
    
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    
    
    context = {
            'form': form     
    }

    return render(request, "accounts/register.html", context)

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})     

def logout_view(request):
    logout(request)
    return redirect("/login")


    #Team views
@login_required(login_url="/login")
def team_detail_view(request, id):
    
    
    team = get_object_or_404(Team,id=id)
    player_list = Player.objects.filter(team=team)
    context = {
        'team': team,
        'player_list': player_list
    }
    return render(request, "team/detail.html", context)
@login_required(login_url="/login")
def team_create_view(request):
    
    form = TeamForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TeamForm()

    context = {
        'form': form
    }
    return render(request, "team/create.html", context)
@login_required(login_url="/login")
def team_update_view(request, id=id):
    obj = get_object_or_404(Team, id=id)
    form = TeamForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "team/create.html", context)

@login_required(login_url="/login")
def team_list_view(request):
    queryset = Team.objects.all()
    context = {
        "object_list" : queryset
    }

    return render(request, "team/list.html", context)



#League views
@login_required(login_url="/login")
def league_detail_view(request, id):
    
    
    league = get_object_or_404(League,id=id)
    team_list = Team.objects.filter(league=league)
    context = {
        'league': league,
        'team_list': team_list
    }
    return render(request, "league/detail.html", context)
@login_required(login_url="/login")
def league_create_view(request):
    
    form = LeagueForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = LeagueForm()

    context = {
        'form': form
    }
    return render(request, "league/create.html", context)
@login_required(login_url="/login")
def league_update_view(request, id=id):
    obj = get_object_or_404(League, id=id)
    form = LeagueForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "league/create.html", context)

@login_required(login_url="/login")
def league_list_view(request):
    queryset = League.objects.all()
    context = {
        "object_list" : queryset
    }

    return render(request, "league/list.html", context)




#Game views
@login_required(login_url="/login")
def game_detail_view(request, id):
    
    
    game = get_object_or_404(Game,id=id)
    
    context = {
        'game': game,
        
    }
    return render(request, "game/detail.html", context)
@login_required(login_url="/login")
def game_create_view(request):
    
    form = GameForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = GameForm()

    context = {
        'form': form
    }
    return render(request, "game/create.html", context)
@login_required(login_url="/login")
def game_update_view(request, id=id):
    obj = get_object_or_404(Game, id=id)
    form = GameForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "game/create.html", context)

@login_required(login_url="/login")
def game_list_view(request):
    queryset = Game.objects.all()
    context = {
        "object_list" : queryset
    }

    return render(request, "game/list.html", context)