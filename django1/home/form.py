from django import forms
from . import models


class Userform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Userform, self).__init__(*args, **kwargs)
        for item in Userform.visible_fields(self):
            if item.label == 'Password':
                item.field.widget.attrs['id'] = 'password'
            item.field.widget.attrs['class'] = 'form-control'

    """
        Name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
        Email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
        Password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    """

    class Meta:
        model = models.User
        fields = ('Email', 'Password')
