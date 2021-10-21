from django.shortcuts import render, redirect, get_object_or_404

from django.utils import timezone
from .models import Review, Ticket
from .forms import CreateReviewForm, TicketForm, CreateResponseReviewForm

def reviews_list(request):

    list_of_T_and_R = []
    reviews = Review.objects.order_by('-time_created')
    tickets = Ticket.objects.order_by('-time_created')

    for review in reviews:
        list_of_T_and_R.append(review)
    for ticket in tickets:
        for review in reviews:
            if ticket == review.ticket:
                ticket.done = True
        list_of_T_and_R.append(ticket)

    ordonnerd_list_of_T_and_R = sorted(list_of_T_and_R, key=lambda k: k.time_created, reverse=True)

    return render(request, 'flux/reviews_list.html', {"list_of_ticket_and_reviews": ordonnerd_list_of_T_and_R})

def make_a_ticket(request):

    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.time_created = timezone.now()
            post.save()

            return redirect('reviews_list')
    else:
        form = TicketForm()

    return render(request, 'flux/make_a_ticket.html', {'form': form})

def create_a_review(request):

    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.time_created = timezone.now()
            post.save()

            reviews_form = CreateReviewForm(request.POST)
            reviews_ticket = Ticket.objects.get(id=post.id)
            post = reviews_form.save(commit=False)
            post.ticket = reviews_ticket
            post.user = request.user
            post.time_created = timezone.now()
            post.save()

            return redirect('reviews_list')

    form_ticket = TicketForm()
    form_review = CreateReviewForm()

    return render(request, 'flux/create_a_review.html', {'form_ticket' : form_ticket, 'form_review': form_review})

def create_response_review(request, id):

    ticket = get_object_or_404(Ticket, id=id)

    if request.method == "POST":
        form = CreateResponseReviewForm(request.POST)
        print(form)
        if form.is_valid():
            post = form.save(commit=False)
            post.ticket = ticket
            post.user = request.user
            post.time_created = timezone.now()
            post.save()

            return redirect('reviews_list')

    form = CreateResponseReviewForm()

    return render(request, 'flux/create_a_review.html', {'form': form})