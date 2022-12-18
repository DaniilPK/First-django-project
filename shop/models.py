from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from django.forms import ModelForm, TextInput, Textarea, FileInput, EmailInput, PasswordInput, HiddenInput


class Tidings(models.Model):
    title = models.CharField('Название статьи', max_length=50)
    content = models.TextField('Описание')
    photo = models.ImageField('Фото', upload_to="photos/%Y/%m/%d/")
    username = models.CharField('Имя пользователя', max_length=250, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_upate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/home'

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'


class TidingsForm(ModelForm):
    class Meta:
        model = Tidings
        fields = ['title', 'content', 'photo', 'username']
        widgets = {
            'title': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Введите название",
                }
            ),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Описание",
                'id': "floatingTextarea2",
                'style': "height: 100px",
            }),
            'photo': FileInput(attrs={
                'class': 'form-control',
                'id': "formFile",
                'accept': 'image/gif,image/jpeg,image/png'
            })
        }


class TidingsFormEdit(ModelForm):
    class Meta:
        model = Tidings
        fields = ['title', 'content', 'photo']
        widgets = {
            'title': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Введите название",
                }
            ),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Описание",
                'id': "floatingTextarea2",
                'style': "height: 100px",
            }),
            'photo': FileInput(attrs={
                'class': 'form-control',
                'id': "formFile",
                'accept': 'image/gif,image/jpeg,image/png'
            })
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин',
                               widget=TextInput(attrs={'class': "form-control", 'placeholder': "username"}))
    email = forms.CharField(label='Email', widget=EmailInput(attrs={'class': "form-control", 'placeholder': "email"}))
    password1 = forms.CharField(label='Пароль 1', widget=TextInput(
        attrs={'type': 'password', 'class': "form-control", 'placeholder': "password"}))
    password2 = forms.CharField(label='Пароль 2', widget=TextInput(
        attrs={'type': 'password', 'class': "form-control", 'placeholder': "password2"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               widget=TextInput(attrs={'class': "form-control", 'placeholder': "username"}))
    password = forms.CharField(label='Пароль', widget=TextInput(
        attrs={'type': 'password', 'class': "form-control", 'placeholder': "password"}))
