from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Review(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='review_photos/%Y/%m/%d', blank=True)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
