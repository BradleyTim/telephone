from django.contrib import admin
from .models import Phone


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'price', 'is_published', 'date_posted')
    list_display_links = ('id', 'name')
    list_filter = ('brand',)
    list_editable = ('is_published',)
    search_fields = ('name', 'brand', 'price', 'operating_system', 'storage', 'ram', 'cpu')
    list_per_page = 25


admin.site.register(Phone, PhoneAdmin)
