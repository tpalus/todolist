from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UzivatelCreationForm

# Create your views here.
class SignUpView(CreateView):
    form_class = UzivatelCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
