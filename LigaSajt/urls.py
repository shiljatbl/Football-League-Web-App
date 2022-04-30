"""LigaSajt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Liga import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('player/<int:id>', views.player_detail_view, name='player-detail'),
    path('player/<int:id>/update/', views.player_update_view, name='update-player'),
    path('player/create/', views.player_create_view, name='create-player'),
    path('players/', views.player_list_view, name='player-list'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('team/<int:id>', views.team_detail_view, name='team-detail'),
    path('team/<int:id>/update/', views.team_update_view, name='update-team'),
    path('team/create/', views.team_create_view, name='create-team'),
    path('teams/', views.team_list_view, name='team-list'),
    path('league/<int:id>', views.league_detail_view, name='league-detail'),
    path('league/<int:id>/update/', views.league_update_view, name='update-league'),
    path('league/create/', views.league_create_view, name='create-league'),
    path('leagues/', views.league_list_view, name='league-list'),
]
