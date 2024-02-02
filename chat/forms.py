"""
Forms for the user views
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "placeholder": "Email",
            "class": "form-control"
        }
    ))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "First Name",
            "class": "form-control"
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Last Name",
            "class": "form-control"
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Password",
            "class": "form-control"
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Password check",
            "class": "form-control"
        }
    ))

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email', 'password1', 'password2')
