from django.shortcuts import render


def bot(request):
    return render(request , 'bot.html')

def contact(request):
    return render(request , 'contact.html')

def feature(request):
    return render(request , 'feature.html')

def index(request):
    return render(request , 'index.html')

def pricing(request):
    return render(request , 'pricing.html')

def services(request):
    return render(request , 'services.html')