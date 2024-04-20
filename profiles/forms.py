from logging import PlaceHolder
from xmlrpc.client import Boolean
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from .models import Profile


class UserRegisterForm(forms.ModelForm):
    password2 = forms.CharField(
                            widget=forms.PasswordInput(attrs={
                                'placeholder':'repeat your password',
                                }), 
                            required=True)
    
    class Meta:
        model = Profile
        fields = ("user", "email", "password", "birthday")
        widgets = {
            'user': forms.TextInput(attrs={
                              'placeholder':'Login',
                           }),
            'email': forms.TextInput(attrs={
                                'placeholder':'Email',
                                }),
            "password": forms.PasswordInput(attrs={
                                'placeholder':'password',
                                }),
            "birthday": forms.DateInput(
                                format="%Y-%m-%d", 
                                attrs={"type": "date",
                                       "placeholder": 'birthday'}),
        }     
        widgets = dict(widgets)

        required = (
            "user", 
            "email", 
            "password",
        )
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UserLoginForm(forms.Form):
    user = forms.CharField(max_length=30, widget= forms.TextInput(
                            attrs={
                                'placeholder':'email or username',
                                }),
                           required=True)
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'password',
            }
        ),
        required=True,
    )

# Create a UserUpdateForm to update a username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# Create a ProfileUpdateForm to update image.
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
