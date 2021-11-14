from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views # import views so we can use them in urls.


urlpatterns = [
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
    name='login'),
    path('logout', views.logout_user, name='logout'),
    path('signup', views.signup_page, name='signup'),

]