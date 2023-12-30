from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Your username',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder' : 'Your email',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Your password',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Confirm password',
    }))

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')