from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class SpotifyLoginView(LoginView):
    template_name = "spotify/login.html"
    success_url = reverse_lazy("home")


# Home view
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "spotify/home.html"
    login_url = "/login"
    