from django import forms
#from django.contrib.auth.models import User
from users.models import User

class RegisterForm(forms.Form):
    usuario = forms.CharField(required=True,
                                min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={'class':'form-control','id':'username','placeholder':'Usuario'}))
    correo = forms.EmailField(required=True,
                                widget=forms.EmailInput(attrs={'class':'form-control','id':'correo','placeholder':'Correo Electronico'}))
    password = forms.CharField(label = 'Contraseña',
                                required=True,
                                widget=forms.PasswordInput(attrs={'class':'form-control','id':'password'}))
    password2 = forms.CharField(label = 'Confirmar Contraseña',
                                required=True,
                                widget=forms.PasswordInput(attrs={'class':'form-control','id':'password2'}))

    def clean_usuario(self):
        usuario = self.cleaned_data.get('usuario')
        if User.objects.filter(username=usuario).exists():
            raise forms.ValidationError('El usuario no se encuentra disponible')
        
        return usuario

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if User.objects.filter(email=correo).exists():
            raise forms.ValidationError('El correo ya se encuentra en uso')
        
        return correo

    def clean(self):#Siempre y cuando se necesite validar campos o atributos que dependan unos de otros
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'La contraseña no coincide')

    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('usuario'),
            self.cleaned_data.get('correo'),
            self.cleaned_data.get('password'),
        )
