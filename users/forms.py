from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Uzivatel

class UzivatelCreationForm(UserCreationForm):

    class Meta(UserChangeForm.Meta):
        model = Uzivatel
        fields = ('username','email','age',)

class UzivatelChangeForm(UserChangeForm):

    class Meta:
        model = Uzivatel
        fields = ('username','email','age',)
