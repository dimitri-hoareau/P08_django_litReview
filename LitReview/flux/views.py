from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Review, Ticket
from .forms import PostForm

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

def ask_for_ticket(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.time_created = timezone.now()
            post.save()

            return redirect('reviews_list')
    else:
        form = PostForm()

    return render(request, 'flux/ask_for_ticket.html', {'form': form})