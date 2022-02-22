from django import forms
from .models import Ticket, Review, UserFollows


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('title', 'description', 'image')


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

        model = UserFollows
        fields = ('followed_user',)
