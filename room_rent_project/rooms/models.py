from django.db import models

class Room(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    facilities = models.TextField(blank=True)
    photo = models.URLField(blank=True, null=True,max_length=500)  # Changed to store URLs

    def __str__(self):
        return self.title