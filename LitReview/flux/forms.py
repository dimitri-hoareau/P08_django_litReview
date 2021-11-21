from django import forms

from .models import Ticket, Review, UserFollows
from django.contrib.auth import get_user_model

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

    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop('user', None)
    #     self.create_form(self.user.id)
    #     super(SubscriptionsForm, self).__init__(*args, **kwargs)

    # def create_form(self, user_id):
    #     User = get_user_model()
    #     users = User.objects.all()
    #     followed_users_models = UserFollows.objects.filter(user=user_id)

    #     queryset_without_hello = User.objects.exclude(pk__in=followed_users_models)

    #     print(queryset_without_hello)

    #     for user in followed_users_models:
    #         print(user.followed_user)

    #     print("======================================================")
        

    #     for user in users:
    #         print(user)

        # self.fields['followed_user'].choices = 
 

