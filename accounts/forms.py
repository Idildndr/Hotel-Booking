from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    country = forms.CharField(max_length=100, required=False)
    city = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ( 'first_name', 'last_name','username', 'email', 'password1', 'password2',  'country', 'city')