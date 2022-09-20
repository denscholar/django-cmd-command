from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Cmdr


class HomePageView(ListView):
    model = Cmdr
    template_name = 'home.html'


