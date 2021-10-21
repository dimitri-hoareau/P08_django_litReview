from django.urls import path
from django.conf.urls import url

from . import views # import views so we can use them in urls.


urlpatterns = [
    path('', views.reviews_list, name='reviews_list'),
    path('make_a_ticket', views.make_a_ticket, name='make_a_ticket'),
    path('create_response_review/<int:id>/', views.create_response_review, name='create_response_review'),
    path('create_a_review', views.create_a_review, name='create_a_review'),

]