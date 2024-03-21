from django import forms
from socialmedia.models import *

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class RegistrationForm(UserCreationForm):

    class Meta:
        model=User
        fields=["username","email","password1",'password2',"first_name"]

class ProfileForm(forms.ModelForm):

    class Meta:
        model=Userprofile
        fields=[
            "bio","dob","gender","phone","profile_pic"
        ]

        widgets = {
            'bio': forms.Textarea(attrs={"class": "form-control","row":"3"}),
            'dob': forms.TextInput(attrs={"class": "form-control " }),
            'gender': forms.Select(attrs={"class": "form-select form-control "}),
            'phone': forms.TextInput(attrs={"class": "form-control "}),
            'profile_pic': forms.FileInput(attrs={"class": "form-control "}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        exclude=['user']
    