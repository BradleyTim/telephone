from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

class Phone(models.Model):
    image = models.ImageField(upload_to='phone_photos/%Y/%m/%d', blank=True)
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    screen = models.CharField(blank=True, max_length=200)
    front_camera = models.CharField(blank=True, max_length=200)
    main_camera = models.CharField(blank=True, max_length=200)
    operating_system = models.CharField(blank=True, max_length=200)
    storage = models.CharField(blank=True, max_length=200)
    ram = models.CharField(blank=True, max_length=200)
    battery = models.CharField(blank=True, max_length=200)
    colors = models.CharField(blank=True, max_length=200)
    cpu = models.CharField(blank=True, max_length=200)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)
