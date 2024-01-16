from django.shortcuts import render
from django.urls import reverse_lazy
import requests
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

from .forms import SignUpForm
from .models import UserProfile
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

    def get_initial(self):
        initial = super().get_initial()
        response = requests.get('https://ipinfo.io')
        data = response.json()
        initial['country'] = data.get('country', '')
        initial['city'] = data.get('city', '')
        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        user_profile = UserProfile(
            user=self.object,
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            country=form.cleaned_data['country'],
            city=form.cleaned_data['city']
        )
        user_profile.save()
        return response
    
    
    
