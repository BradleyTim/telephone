from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'date_posted', 'author')
    list_display_links = ('id', 'title')
    list_filter = ('author',)
    list_editable = ('is_published',)
    search_fields = ('title', 'author')
    list_per_page = 25

admin.site.register(Review, ReviewAdmin)
