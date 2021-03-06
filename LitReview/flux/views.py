from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Review, Ticket, UserFollows
from .forms import CreateReviewForm, TicketForm, CreateResponseReviewForm, SubscriptionsForm


@login_required
def reviews_list(request):
    user_id = request.user.id
    followed_users_models = UserFollows.objects.filter(user=user_id)
    str_followed_users = []

    for user in followed_users_models:
        str_followed_users.append(str(user.followed_user))
    list_of_T_and_R = []
    reviews = Review.objects.order_by('-time_created')
    tickets = Ticket.objects.order_by('-time_created')

    for review in reviews:
        if str(review.user) in str_followed_users or str(review.user) == str(request.user):
            list_of_T_and_R.append(review)
    for ticket in tickets:
        if str(ticket.user) in str_followed_users or str(ticket.user) == str(request.user):
            for review in reviews:
                if ticket == review.ticket:
                    ticket.done = True
            list_of_T_and_R.append(ticket)

    ordonnerd_list_of_T_and_R = sorted(list_of_T_and_R, key=lambda k: k.time_created, reverse=True)

    return render(request, 'flux/reviews_list.html', {"list_of_ticket_and_reviews": ordonnerd_list_of_T_and_R})


@login_required
def posts(request):

    list_of_T_and_R = []
    reviews = Review.objects.filter(user=request.user).order_by('-time_created')
    tickets = Ticket.objects.filter(user=request.user).order_by('-time_created')

    for review in reviews:
        list_of_T_and_R.append(review)
    for ticket in tickets:
        for review in reviews:
            if ticket == review.ticket:
                ticket.done = True
        list_of_T_and_R.append(ticket)

    ordonnerd_list_of_T_and_R = sorted(list_of_T_and_R, key=lambda k: k.time_created, reverse=True)

    return render(request, 'flux/reviews_list.html', {"list_of_ticket_and_reviews": ordonnerd_list_of_T_and_R, "posts_list": True})


@login_required
def subscriptions(request):

    followed_users = []
    str_followed_users = []
    following_users = []

    user_id = request.user.id
    followed_users_models = UserFollows.objects.filter(user=user_id)
    following_users_models = UserFollows.objects.filter(followed_user=user_id)
    for user in followed_users_models:
        followed_users.append(user)
        str_followed_users.append(user.followed_user)
    for user in following_users_models:
        following_users.append(user)

    if request.method == "POST":
        form = SubscriptionsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user

            if post.followed_user in str_followed_users:
                error_message = "Vous suivez d??j?? cet utilisateur"
                return render(request, 'flux/subscriptions.html', {'form': form, "followed_users": followed_users, "following_users": following_users, "error": error_message})
            elif post.followed_user == request.user:
                error_message = "Vous ne pouvez pas vous suivre vous-m??me"
                return render(request, 'flux/subscriptions.html', {'form': form, "followed_users": followed_users, "following_users": following_users, "error": error_message})
            else:
                post.save()
                return redirect('subscriptions')
    else:
        form = SubscriptionsForm()

    return render(request, 'flux/subscriptions.html', {'form': form, "followed_users": followed_users, "following_users": following_users})


@login_required
def make_a_ticket(request):

    print(request.path)
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.time_created = timezone.now()
            post.save()

            return redirect('reviews_list')
    else:
        form = TicketForm()

    return render(request, 'flux/make_a_ticket.html', {'form': form})


@login_required
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

    return render(request, 'flux/create_a_review.html', {'form_ticket': form_ticket, 'form_review': form_review})


@login_required
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


@login_required
def post_remove(request, type, id):

    if type == 'ticket':
        post = get_object_or_404(Ticket, id=id)
    else:
        post = get_object_or_404(Review, id=id)
    post.delete()

    return redirect('posts')


@login_required
def post_update(request, type, id):

    if request.method == "POST":
        if type == 'ticket':
            form = TicketForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)

                Ticket.objects.filter(id=id).update(title=post.title)
                Ticket.objects.filter(id=id).update(description=post.description)
        else:
            form = CreateResponseReviewForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)

                Review.objects.filter(id=id).update(headline=post.headline)
                Review.objects.filter(id=id).update(body=post.body)
                Review.objects.filter(id=id).update(rating=post.rating)

        return redirect('posts')

    else:
        if type == 'ticket':
            ticket = get_object_or_404(Ticket, id=id)
            form = TicketForm(initial={'title': ticket.title, 'description': ticket.description},)
        else:
            ticket = get_object_or_404(Review, id=id)
            form = CreateResponseReviewForm(initial={'headline': ticket.headline, 'body': ticket.body, 'rating': ticket.rating},)

    return render(request, 'flux/make_a_ticket.html', {'form': form, 'update': True})


@login_required
def follower_remove(reques, id):

    post = get_object_or_404(UserFollows, id=id)
    post.delete()

    return redirect('subscriptions')
