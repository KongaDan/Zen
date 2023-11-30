from django import forms
from django.contrib.auth import get_user_model
from .models import *
from django.contrib.admin.widgets import AdminSplitDateTime
from django.contrib.auth.forms import UserCreationForm as UCF

class CustomUserForm(UCF):
    class Meta:
        model=get_user_model()
        fields=['username','email','section','promotion']

class TacheForm(forms.ModelForm):
    heure_fin=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placeholder': '01/01/2023 12:00'}),
        help_text='Entrez une date et une heure au format JJ/MM/AAAA HH:MM')
    class Meta:
        model=Tache
        fields=['nom','description','heure_fin']
        exclude=['heure_creation']
        widgets={
            'heure_fin':AdminSplitDateTime(),
        }

class UserCreationChangeForm(forms.ModelForm):
    class Meta:
        model=get_user_model()
        fields=['username','email','last_name','first_name','numero','section','promotion']

class UserDeleteform(forms.Form):
    delete=forms.BooleanField(
        label="Je suis conscient que la suppresion de mon compte est une action definitive "
        )
