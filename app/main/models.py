from django.db import models


class Smartphone(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/', blank=False)
    date = models.DateTimeField(blank=True, null=True)
    panel_type = models.CharField(max_length=100, blank=False, null=False, default=None)
    resolution = models.CharField(max_length=100, blank=False, null=False, default=None)
    number_of_cores = models.CharField(max_length=100, blank=False, null=False, default=None)
    aspect_ratio = models.CharField(max_length=100, blank=False, null=False, default=None)
    pixel_density = models.CharField(max_length=100, blank=False, null=False, default=None)
    update_frequency = models.CharField(max_length=100, blank=False, null=False, default=None)
    clock_frequency = models.CharField(max_length=100, blank=False, null=False, default=None)
