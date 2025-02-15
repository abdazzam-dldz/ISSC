from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from app.models import User, Post




class RegisForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        error_messages = {
            'username': {
                'required': 'username pengguna harus diisi.',
                'unique': 'username telah digunakan.',
            },
            'email': {
                'required': 'Email harus diisi.',
                'invalid': 'masukkan email yang valid.',
                'unique': 'email telah digunakan.',
            },
            'password1': {
                'required': 'password harus diisi.',
                'too_short': 'password terlalu minimal 8 karakter.',
            },
            'password2': {
                'required': 'konfirmasi password harus diisi.',
            },
        }

    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError('konfirmasi password tidak sesuai.')
        return password2

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise ValidationError('password minimal 8 karakter.')
        return password1


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['message']

    
