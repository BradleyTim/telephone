from django.shortcuts import render
from .models import Phone

def index(request):
    context = {
        'phones': Phone.objects.all()
    }
    return render(request, 'pages/index.html', context)
