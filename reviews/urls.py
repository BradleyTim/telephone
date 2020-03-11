from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='reviews'),
    path('reviews/<int:review_id>', views.review_details, name='review-details'),
]