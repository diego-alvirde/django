from django import forms

class RegisterForm(forms.Form):
    usuario = forms.CharField(required=True,
                                min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={'class':'form-control','id':'username','placeholder':'Usuario'}))
    correo = forms.EmailField(required=True,
                                widget=forms.EmailInput(attrs={'class':'form-control','id':'correo','placeholder':'Correo Electronico'}))
    password = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'class':'form-control','id':'password','placeholder':'Password'}))