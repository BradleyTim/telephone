from django.shortcuts import render, get_object_or_404
from shop.models import Phone


def index(request):
    context = {
        'phones': Phone.objects.all(),
        'title': 'Phones'
    }
    return render(request, 'pages/index.html', context)


def phone_details(request, phone_id):
    context = {
        'phone': get_object_or_404(Phone, pk=phone_id)
    }
    return render(request, 'pages/phone-details.html', context)


def about(request):
    return render(request, 'pages/about.html', {'title': 'About'})
