from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pages-index'),
    path('products/<int:phone_id>', views.phone_details, name='pages-product-detail'),
    path('about/', views.about, name='pages-about'),
]