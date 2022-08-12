from django import forms
from .models import Users


class usersForm(forms.ModelForm):
    
    class Meta:
        model = Users
        fields = ['username', 'email']
        
class passwordForm(forms.Form):
    password = forms.CharField(required=True, widget=forms.PasswordInput)