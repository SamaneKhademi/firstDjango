from django import forms

class Userform(forms.Form):
    Name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))