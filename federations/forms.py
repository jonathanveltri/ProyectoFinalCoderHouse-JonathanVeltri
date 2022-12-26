from django import forms
from federations.models import Federation

class FederationForm(forms.Form):
    name = forms.CharField(
        label="Nombre de la federación",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "federation-name",
                "placeholder": "Nombre de la federación",
                "required": "True",
            }
        ),
    )
    initials = forms.CharField(
        label="Sigla de la federación",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "federations-initials",
                "placeholder": "Sigla de la federación",
                "required": "True",
            }
        ),
    )
    official_website = forms.CharField(
        label="Sitio oficial",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "federations-website",
                "placeholder": "Sitio oficial",
                "required": "True",
            }
        ),
    )
    image = forms.ImageField(required=False)

    class Meta:
        model = Federation
        fields = ["name", "initials", "official_website", "image"]
    