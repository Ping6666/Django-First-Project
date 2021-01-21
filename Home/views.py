from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

from .models import homepagesDataset


class homepagesListView(ListView):
    template_name = 'homepage_list.html'
    queryset = homepagesDataset.objects.all()