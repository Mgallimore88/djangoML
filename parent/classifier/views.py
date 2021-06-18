from django.shortcuts import render
from django.views.generic import ListView
from classifier.models import Image

# Create your views here.

class ImageListView(ListView):
    model = Image
    