from django.forms import fields
from ewaste.models import Phones
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required = True, max_length='30')
    contact = forms.IntegerField(required = True)
    class Meta:
        model = User
        fields = ['username','email','contact','password1','password2']

class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField(required = True, max_length='25')

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    contact = forms.CharField(required=True)
    class Meta:
        model = Profile
        fields = ['contact','image']



