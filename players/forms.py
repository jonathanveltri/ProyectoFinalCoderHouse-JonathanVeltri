from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from players.models import Player

class PlayerForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "player-name",
                "placeholder": "Nombre",
                "required": "True",
            }
        ),
    )
    last_name = forms.CharField(
        label="Apellido",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "player-last_name",
                "placeholder": "Apellido",
                "required": "True",
            }
        ),
    )
    team = forms.CharField(
        label="Equipo",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "team-name",
                "placeholder": "Equipo",
                "required": "True",
            }
        ),
    )
    number = forms.IntegerField(
        label="Número",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "number-name",
                "placeholder": "Número",
                "required": "True",
            }
        ),
    )
    position = forms.CharField(
        label="Posición",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "position-name",
                "placeholder": "Posición",
                "required": "True",
            }
        ),
    )
    class Meta:
        model = Player
        fields = ["name", "last_name", "team", "number", "position"] 
    

class CommentForm(forms.Form):
    comment_text = forms.CharField(
        label="",
        required=False,
        max_length=500,
        min_length=10,
        strip=True,
        widget=forms.Textarea(
            attrs={
                "class": "comment-text",
                "placeholder": "Ingrese su comentario...",
                "required": "True",
                "max_length": 500,
                "min_length": 10,
                "rows": 2,
                "cols": 10,
                "style":"min-width: 100%",
            }
        ),
    )