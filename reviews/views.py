from django.shortcuts import render, get_object_or_404
from .models import Review

def index(request):
    context = {
        'reviews': Review.objects.all()
    }
    return render(request, 'reviews/reviews.html', context)


def review_details(request, review_id):
    context = {
        'review': get_object_or_404(Review, pk=review_id)
    }
    return render(request, 'reviews/review-details.html', context)