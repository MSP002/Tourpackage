from django.contrib import admin

# Register your models here.
from .models import TourPackage, Itinerary

class ItineraryInline(admin.TabularInline):
    model = Itinerary
    extra = 5

@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'duration')
    search_fields = ('title', 'location')
    inlines = [ItineraryInline]

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ('tour_package', 'day_number', 'title', 'transportation')
    list_filter = ('tour_package',)