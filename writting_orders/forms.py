from django.contrib.auth.models import User
from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import User, Order


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']





class OrderCreateForm(forms.ModelForm):

    class Meta:

        model = Order

        exclude = ('user',)

        fields = ['type', 'academic', 'topic', 'pages', 'urgency', 'format', 'instructions', 'pdf',]