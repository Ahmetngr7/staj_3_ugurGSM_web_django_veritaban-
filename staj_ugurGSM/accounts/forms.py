from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    sehir = forms.ChoiceField(choices=Profile.SEHIR_SECENEKLERI, required=True)
    telefon = forms.CharField(required=False)
    adres = forms.CharField(widget=forms.Textarea, required=False)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Lütfen geçerli bir gmail adresi giriniz.")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bu email zaten kayıtlı.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile = Profile.objects.get(kullanici=user)
            profile.sehir = self.cleaned_data['sehir']
            profile.telefon = self.cleaned_data['telefon']
            profile.adres = self.cleaned_data['adres']
            profile.save()
        return user
