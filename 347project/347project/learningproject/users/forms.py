from django import forms
from .models import Profile, ContactUs
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name',
            'bio',
            'profession',
            'birth_date',
            'image',
        ]


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = [
            'name',
            'email',
            'describe',
        ]

