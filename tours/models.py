
# Create your models here.
from django.db import models

class TourPackage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField(help_text="Duration in days")
    location = models.CharField(max_length=255)
    featured_image = models.ImageField(upload_to='tour_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class Itinerary(models.Model):
    tour_package = models.ForeignKey(TourPackage, related_name='itineraries', on_delete=models.CASCADE)
    day_number = models.PositiveIntegerField(help_text="Day number in the itinerary")
    title = models.CharField(max_length=255)
    description = models.TextField()
    included_meals = models.CharField(max_length=255, blank=True, help_text="Comma separated: breakfast, lunch, dinner")
    transportation = models.CharField(max_length=255, blank=True)
    attractions = models.TextField(help_text="Comma-separated attractions", blank=True)

    class Meta:
        unique_together = ('tour_package', 'day_number')
        ordering = ['day_number']

    def __str__(self):
        return f"Day {self.day_number}: {self.title}"