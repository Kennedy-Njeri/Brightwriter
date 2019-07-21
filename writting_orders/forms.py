from django.contrib.auth.models import User
from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import User, Order
from tinymce import TinyMCE




class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False




class RegistrationForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class OrderCreateForm(forms.ModelForm):

    instructions = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:

        model = Order

        exclude = ('user',)

        fields = ['type', 'academic', 'topic', 'pages', 'urgency', 'format', 'instructions', 'pdf', 'email']