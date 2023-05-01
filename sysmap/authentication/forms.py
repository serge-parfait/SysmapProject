from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Nom d'utilisateur")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Mot de passe")
