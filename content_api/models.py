from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/', blank=True)
