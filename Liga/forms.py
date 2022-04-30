from socket import fromshare
from django import forms
from .models import Player, Team, League
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            'name',
            'team',
            'age',
            'position',
            'iscaptain'

        ]

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            'name',
            'league'

        ]

class LeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = [
            'name',
            'description',
            'no_of_teams',
            'country',
            'season',
            'year'

        ]


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
            

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))