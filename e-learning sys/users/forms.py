from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from e_learning.forms import BootstrapFormMixin

from .models import User


class RegistrationForm(BootstrapFormMixin, UserCreationForm):
    role = forms.ChoiceField(choices=User.Role.choices)

    class Meta:
        model = User
        fields = ["username", "email", "role", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None


class LoginForm(BootstrapFormMixin, AuthenticationForm):
    pass
