from django import forms
from django.forms import fields

from .models import Ticket, Review

class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('title', 'description')

class CreateTicketForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('ticket', 'headline', 'body', 'rating')