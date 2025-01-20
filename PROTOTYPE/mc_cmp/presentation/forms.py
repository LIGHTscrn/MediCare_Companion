from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=[('patient', 'Patient'), ('caregiver', 'Caregiver')])

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'role']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
