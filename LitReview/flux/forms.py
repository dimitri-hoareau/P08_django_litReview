from django import forms
from django.forms import fields

from .models import Ticket

class PostForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('title', 'description')