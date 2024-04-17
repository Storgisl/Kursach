from logging import PlaceHolder
from xmlrpc.client import Boolean
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(forms.Form):
    email = forms.EmailField(widget= forms.TextInput(
                            attrs={
                                'placeholder':'Email',
                                }),)
    username = forms.CharField(
                        max_length=30, 
                        required=True,
                        widget= forms.TextInput
                           (attrs={
                               'placeholder':'Login',
                               }))
    
    password1 = forms.CharField(
                            widget=forms.PasswordInput(attrs={
                                'placeholder':'password',
                                }), 
                            required=True)
    
    password2 = forms.CharField(
                            widget=forms.PasswordInput(attrs={
                                'placeholder':'repeat your password',
                                }), 
                            required=True)
    
    birthday = forms.DateField(label="Date of Birth",
                                required=True,
                                widget=forms.DateInput(
                                format="%Y-%m-%d", attrs={"type": "date"}),
                                input_formats=["%Y-%m-%d"])
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget= forms.TextInput(
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
