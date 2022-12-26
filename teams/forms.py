from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from federations.models import Federation
from datetime import datetime

MONTHS = {
    1:'enero', 2:'febrero', 3:'marzo', 4:'abril',
    5:'mayo', 6:'junio', 7:'julio', 8:'agosto',
    9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'
}

class TeamForm(forms.Form):
    name = forms.CharField(
        label="Nombre del equipo",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "team-name",
                "placeholder": "Nombre del equipo",
                "required": "True",
            }
        ),
    )
    federation = forms.ModelChoiceField(queryset= Federation.objects.all(),
        label="Federacion de pertenencia",
        required=False,
        widget=forms.Select(
            attrs={
                "class": "federation-name",
                "placeholder": "Federacion de pertenencia",
                "required": "True",
            }
        ),
    )
    country = forms.CharField(
        label="Pais de origen",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "country-name",
                "placeholder": "Pais de origen",
                "required": "True",
            }
        ),
    )
    city = forms.CharField(
        label="Ciudad",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "country-name",
                "placeholder": "Ciudad",
                "required": "True",
            }
        ),
    )
    fundation_date = forms.DateField(label='Fecha de fundación', 
                                    required=False,
                                    widget=forms.SelectDateWidget(
                                        years=range(1900, datetime.today().year),
                                        months = MONTHS,
                                        empty_label=("Año", "Mes", "Dia"),
                                    ),
    )
    