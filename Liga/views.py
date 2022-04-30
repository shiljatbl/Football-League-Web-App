from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Player
from .forms import NewUserForm, PlayerForm, LoginForm
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
    return render(request, "index.html", my_context)

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
            return redirect('login')
    
    
    context = {
            'form': form     
    }

    return render(request, "register.html", context)

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

    return render(request, "login.html", {"form": form, "msg": msg})     

def logout_view(request):
    logout(request)
    return redirect("/login")