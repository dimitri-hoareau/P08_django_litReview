from django import forms
from django.forms import fields

from .models import Ticket


# par convention on donne le nom du model : PostForm = TicketForm
class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('title', 'description')