from django.urls import path
from django.conf.urls import url

from . import views # import views so we can use them in urls.


urlpatterns = [
    path('', views.reviews_list, name='reviews_list'),
    path('ask_for_ticket', views.ask_for_ticket, name='ask_for_ticket'),

]