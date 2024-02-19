from django.shortcuts import render
from .models import Smartphones

def home(request):
    return render(request, 'home_page.html')

def smartphones(request):
    smartphones = Smartphones.objects.all()
    return render(request, 'smartphones.html', {'smartphones': smartphones})