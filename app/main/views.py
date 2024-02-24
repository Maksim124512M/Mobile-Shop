from django.shortcuts import render
from .models import Smartphone
from django.views.generic import DetailView

def home(request):
    return render(request, 'home_page.html')

def smartphones(request):
    smartphones = Smartphone.objects.order_by('date__minute')
    return render(request, 'smartphones.html', {'smartphones': smartphones})

def smartphone_detail(request, id):
    smartphones = Smartphone.objects.get(id=id)
    context = {
        'smartphones': smartphones,
    }
    return render(request, 'smartphone_detail.html', context)