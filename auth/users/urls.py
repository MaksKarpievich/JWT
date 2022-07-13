from django.contrib import admin
from django.urls import path
from .views import RegisterView, LoginView,Userview,Logout


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', Userview.as_view()),
    path('Logout', Logout.as_view())

]