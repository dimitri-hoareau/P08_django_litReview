from django.urls import path

from . import views # import views so we can use them in urls.


urlpatterns = [
    path('', views.LoginPageView.as_view(), name='login'),
    path('logout', views.logout_user, name='logout'),

]