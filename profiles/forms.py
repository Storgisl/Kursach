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

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email'}),
        }
        widgets = dict(widgets)

    def clean_password2(self):
        password1 = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password1 and password1 != password2:
            raise ValidationError('Passwords do not match.')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('birthday',)
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

    def save(self, commit=True, user=None):
        profile = super(ProfileRegisterForm, self).save(commit=False)
        if user:
            profile.user = user
        if commit:
            profile.save()
        return profile
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
