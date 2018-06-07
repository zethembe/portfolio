from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    text = models.TextField(max_length=1000)
    created = models.DateField(default=timezone.now())
    photo = models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
        return self.title

