from django.shortcuts import render
from .models import Review

def index(request):
    context = {
        'reviews': Review.objects.all()
    }
    return render(request, 'reviews/reviews.html', context)
