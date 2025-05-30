from django import forms
from .models import TourPackage, Itinerary

class TourPackageForm(forms.ModelForm):
    class Meta:
        model = TourPackage
        fields = ['title', 'description', 'price', 'duration', 'location', 'featured_image']

class ItineraryForm(forms.ModelForm):
    class Meta:
        model = Itinerary
        fields = ['tour_package', 'day_number', 'title', 'description', 'included_meals', 'transportation', 'attractions']
        extra =5