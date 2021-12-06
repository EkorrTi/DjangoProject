from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from .models import Account
from article.models import Posts
 
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. A valid email address')
    
    class Meta:
        model = Account
        fields = ["email", "username", "password1","password2"]
        labels = {
            'email': "Email", 
            "username": "Username",
            "Password":"Password",
        }

class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
    class Meta:
        model = Account
        fields = ('email', 'password')
    
    # Used before commiting?
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Login')

class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'username')
    
    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % account.email)
    
    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" is already in use.' % account.username)

class MakePostForm(forms.ModelForm):
    text = forms.Textarea()
    class Meta:
        model = Posts
        fields = ('text',)
        exclude = ('user', 'time',)