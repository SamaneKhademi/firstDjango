from django import forms

class User(forms.Form):
    Name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'name'}))
    Email = forms.EmailField()
    Password = forms.CharField(widget=forms.PasswordInput)