from socket import fromshare
from django import forms
from .models import Player


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
