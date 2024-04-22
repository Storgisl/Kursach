from logging import PlaceHolder
from xmlrpc.client import Boolean
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from .models import Profile


class UserRegisterForm(UserCreationForm):#forms.ModelForm
    birthday = forms.DateField(widget=forms.DateInput(
                                    format="%Y-%m-%d", 
                                    attrs={"type": "date",
                                        "placeholder": 'birthday'}),)
    
    class Meta:
            model=User
            fields = ['username','email','password1','password2'] 
            widgets = {
                'username': forms.TextInput(attrs={
                                'placeholder':'Login',
                            }),
                'email': forms.EmailInput(attrs={
                                    'placeholder':'Email',
                                    }),
                "password1": forms.PasswordInput(attrs={
                                    'placeholder':'password',
                                    }),
                "password1": forms.PasswordInput(attrs={
                                    'placeholder':'repeat your password',
                                    }),
            }     
            widgets = dict(widgets)

            required = (
                "user", 
                "email", 
                "password1",
                "password2",
            )
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
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
