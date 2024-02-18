from django.shortcuts import render


def home(request):
    return render(request, 'home_page.html')

def smartphones(request):
    return render(request, 'smartphones.html')