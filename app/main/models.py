from django.db import models


class Smartphones(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/media/', blank=False)
