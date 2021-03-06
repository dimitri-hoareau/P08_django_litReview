from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews_list, name='reviews_list'),
    # path('/<parameyre all ou filter_user>', views.reviews_list, name='reviews_list'),   # + condition dans la vue si all /filter_user
    path('posts', views.posts, name='posts'),
    path('subscriptions', views.subscriptions, name='subscriptions'),
    path('make_a_ticket', views.make_a_ticket, name='make_a_ticket'),
    path('create_response_review/<int:id>/', views.create_response_review, name='create_response_review'),
    path('create_a_review', views.create_a_review, name='create_a_review'),
    path('post/<type>/<id>/remove/', views.post_remove, name='post_remove'),
    path('post/<type>/<id>/update/', views.post_update, name='post_update'),
    path('subscriptions/<id>/remove/', views.follower_remove, name='follower_remove'),
]
