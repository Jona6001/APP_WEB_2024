from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text="Introduce una dirección de correo válida.",
        widget=forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
        }
        help_texts = {
            'username': 'Requerido. 150 caracteres o menos. Solo letras, números y @/./+/-/_',
            'password1': 'Debe contener al menos 8 caracteres.',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) < 2:
            raise forms.ValidationError("El nombre debe contener al menos 2 caracteres.")
        return first_name
