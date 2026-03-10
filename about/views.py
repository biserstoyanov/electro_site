from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def about(request):
    return render(request, "templates/about.html")
