from django import forms

class User(forms.Form):
    Name = forms.CharField(required=True, widget=forms.TextInput())
    Email = forms.EmailField(widget=forms.EmailInput())
    Password = forms.CharField(widget=forms.PasswordInput)