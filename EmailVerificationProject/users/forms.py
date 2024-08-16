from django import forms
from .models import User
import random

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.verification_code = str(random.randint(1000, 9999))
        if commit:
            user.save()
            # Enviar o email com o código de verificação
            self.send_verification_email(user)
        return user

    def send_verification_email(self, user):
        subject = 'Seu código de verificação'
        message = f'Seu código de verificação é: {user.verification_code}'
        user.email_user(subject, message)
