from django import forms


class CreateUserForm(forms.Form):
    username = forms.CharField(label='Username',max_length=15)
    email = forms.EmailField(label='Email',max_length=150)
    password = forms.CharField(widget=forms.PasswordInput(),label='Passoword',max_length=255)
