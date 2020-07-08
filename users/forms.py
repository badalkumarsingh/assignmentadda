from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import UserProfile
from django import forms

class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = {
            'email',
            'first_name',
            'last_name',
            'password',
        }
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = {
            'description',
            'city',
            'website',
            'phone',
            'image',
        }