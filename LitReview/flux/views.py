from django.shortcuts import render
from .models import Review

def post_list(request):
    reviews = Review.objects.order_by('-time_created')
    return render(request, 'flux/reviews_list.html', {'reviews': reviews})