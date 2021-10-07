from django.shortcuts import render
from .models import Review, Ticket

import logging
log = logging.getLogger()

def post_list(request):

    list_of_T_and_R = []
    reviews = Review.objects.order_by('-time_created')
    tickets = Ticket.objects.order_by('-time_created')
    for review in reviews:
        list_of_T_and_R.append(review)
    for ticket in tickets:
        list_of_T_and_R.append(ticket)

    ordonnerd_list_of_T_and_R = sorted(list_of_T_and_R, key=lambda k: k.time_created, reverse=True)

    for element in ordonnerd_list_of_T_and_R:
        print(element)

    return render(request, 'flux/reviews_list.html', {'reviews': reviews, "tickets": tickets, "list_of_ticket_and_reviews": ordonnerd_list_of_T_and_R})