from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UzivatelChangeForm,UzivatelCreationForm
from .models import Uzivatel

class UzivatelAdmin(UserAdmin):
    add_form = UzivatelCreationForm
    form = UzivatelChangeForm
    model = Uzivatel
    list_display = ['email','username','age','is_staff',]

admin.site.register(Uzivatel,UzivatelAdmin)
