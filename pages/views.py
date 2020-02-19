from django.shortcuts import render
from shop.models import Phone

# phones = [
#     {
#         'id': 1,
#         'name': 'samsung galaxy s20',
#         'brand': 'samsung',
#         'price': '$1000'
#     },
#     {
#         'id': 2,
#         'name': 'samsung galaxy s20',
#         'brand': 'samsung',
#         'price': '$1000'
#     },
#     {
#         'id': 3,
#         'name': 'samsung galaxy s20',
#         'brand': 'samsung',
#         'price': '$1000'
#     },
#     {
#         'id': 4,
#         'name': 'samsung galaxy s20',
#         'brand': 'samsung',
#         'price': '$1000'
#     },
#     {
#         'id': 5,
#         'name': 'samsung galaxy s20',
#         'brand': 'samsung',
#         'price': '$1000'
#     },
#     {
#         'id': 6,
#         'name': 'samsung galaxy s20',
#         'brand': 'samsung',
#         'price': '$1000'
#     },
#     {
#         'id': 7,
#         'name': 'samsung galaxy s20',
#         'brand': 'samsung',
#         'price': '$1000'
#     },
#     {
#         'id': 8,
#         'name': 'samsung galaxy s20',
#         'brand': 'samsung',
#         'price': '$1000'
#     },
#     {
#         'id': 9,
#         'name': 'samsung galaxy s20',
#         'brand': 'samsung',
#         'price': '$1000'
#     },
#     {
#         'id': 10,
#         'name': 'samsung galaxy s20',
#         'brand': 'samsung',
#         'price': '$1000'
#     },
#     {
#         'id': 11,
#         'name': 'samsung galaxy s20',
#         'brand': 'samsung',
#         'price': '$1000'
#     },
#     {
#         'id': 11,
#         'name': 'samsung galaxy s20',
#         'brand': 'samsung',
#         'price': '$1000'
#     },
#     {
#         'id': 11,
#         'name': 'samsung galaxy s20',
#         'brand': 'samsung',
#         'price': '$1000'
#     },
#     {
#         'id': 11,
#         'name': 'samsung galaxy s20',
#         'brand': 'samsung',
#         'price': '$1000'
#     },
#     {
#         'id': 11,
#         'name': 'samsung galaxy s20',
#         'brand': 'samsung',
#         'price': '$1000'
#     },
# ]

def index(request):
    context = {
        'phones': Phone.objects.all(),
        'title': 'Phones'
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html', {'title': 'About'})
