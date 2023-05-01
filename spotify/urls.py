from django.urls import path
from .views import SpotifyLoginView, HomeView

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("login/", SpotifyLoginView.as_view(), name='login'),

]
