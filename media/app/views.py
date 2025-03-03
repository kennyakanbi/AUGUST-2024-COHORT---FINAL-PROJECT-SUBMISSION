import urllib.request
import json
from django.shortcuts import render # type: ignore

def index(request):
     return render(request, 'main/index.html')

def about(request):
     return render(request, 'main/about.html')

def contact(request):
     return render(request, 'main/contact.html')