from cProfile import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import  ModelForm
from webApp.models import Profile
from webApp.models import *

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )
    def save(self, commit=True):
        User = super(RegistrationForm, self).save(commit=False)
        User.first_name = self.cleaned_data['first_name']
        User.last_name = self.cleaned_data['last_name']
        User.email = self.cleaned_data['email']
        if commit:
                User.save()
        return User
        
    # def save(self, commit=True):
    #     user = super(RegistrationForm, self).save(commit=False)
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     user.email = self.cleaned_data['email']
        
    #     if commit:
    #         user.save()
    #     return user
class EditProfileForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                 )

class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (     
            'first_name',
            'last_name',
            'email' ,         
            'gender',
            'height',
            'weight',
            'activitylevel'
           )
