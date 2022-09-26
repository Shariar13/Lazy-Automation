from importlib.resources import path
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin



def home(request):
    return render (request, "index.html")

def virtual_assistant (request):
    return render (request, "virtual_assistant.html")