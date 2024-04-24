from logging import PlaceHolder
from xmlrpc.client import Boolean
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError, widgets
from .models import Profile


from django import forms
from .models import Profile

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                                    'placeholder':'password',
                                    }),
                                    required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
                                    'placeholder':'repeat your password',
                                    }),
                                    required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={
                                    'placeholder': 'username'
    }))
    birthday = forms.DateField(input_formats=['%d-%m-%Y'])
    class Meta:
        model = Profile
        fields = ['username', 'email', 'password', 'birthday']

    def clean_password2(self):
        password1 = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password1 and password1 != password2:
            raise ValidationError('Passwords do not match.')
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )
        profile = super().save(commit=False)
        profile.user = user
        profile.birthday = self.cleaned_data['birthday']
        if commit:
            profile.save()
            user.save()
        return user

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
