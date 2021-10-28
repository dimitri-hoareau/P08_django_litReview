from django import forms
from django.forms import fields

from .models import Ticket, Review

class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('title', 'description')

class CreateReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('headline', 'body', 'rating')

class CreateResponseReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('headline', 'body', 'rating')

class SubscriptionsForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('headline',)