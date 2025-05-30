from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from .models import TourPackage, Itinerary
from .forms import TourPackageForm, ItineraryForm

# --- TourPackage Views ---

def tour_package_list(request):
    packages = TourPackage.objects.all()
    return render(request, 'tours/tour_package_list.html', {'packages': packages})

def tour_package_detail(request, pk):
    package = get_object_or_404(TourPackage, pk=pk)
    itineraries = package.itineraries.all()
    return render(request, 'tours/tour_package_detail.html', {'package': package, 'itineraries': itineraries})

def tour_package_create(request):
    if request.method == 'POST':
        form = TourPackageForm(request.POST, request.FILES)
        if form.is_valid():
            package = form.save()
            return redirect('tours:tour_package_detail', pk=package.pk)
    else:
        form = TourPackageForm()
    return render(request, 'tours/tour_package_form.html', {'form': form, 'action': 'Create'})

def tour_package_update(request, pk):
    package = get_object_or_404(TourPackage, pk=pk)
    if request.method == 'POST':
        form = TourPackageForm(request.POST, request.FILES, instance=package)
        if form.is_valid():
            package = form.save()
            return redirect('tours:tour_package_detail', pk=package.pk)
    else:
        form = TourPackageForm(instance=package)
    return render(request, 'tours/tour_package_form.html', {'form': form, 'action': 'Update'})

def tour_package_delete(request, pk):
    package = get_object_or_404(TourPackage, pk=pk)
    if request.method == 'POST':
        package.delete()
        return redirect('tours:tour_package_list')
    return render(request, 'tours/tour_package_confirm_delete.html', {'package': package})

# --- Itinerary Views ---

def itinerary_create(request, package_pk):
    package = get_object_or_404(TourPackage, pk=package_pk)
    if request.method == 'POST':
        form = ItineraryForm(request.POST)
        if form.is_valid():
            itinerary = form.save(commit=False)
            itinerary.tour_package = package
            itinerary.save()
            return redirect('tours:tour_package_detail', pk=package.pk)
    else:
        form = ItineraryForm(initial={'tour_package': package})
    form.fields['tour_package'].widget = forms.HiddenInput()
    return render(request, 'tours/itinerary_form.html', {'form': form, 'action': 'Add', 'package': package})

def itinerary_update(request, pk):
    itinerary = get_object_or_404(Itinerary, pk=pk)
    package = itinerary.tour_package
    if request.method == 'POST':
        form = ItineraryForm(request.POST, instance=itinerary)
        if form.is_valid():
            form.save()
            return redirect('tours:tour_package_detail', pk=package.pk)
    else:
        form = ItineraryForm(instance=itinerary)
    form.fields['tour_package'].widget = forms.HiddenInput()
    return render(request, 'tours/itinerary_form.html', {'form': form, 'action': 'Update', 'package': package})

def itinerary_delete(request, pk):
    itinerary = get_object_or_404(Itinerary, pk=pk)
    package = itinerary.tour_package
    if request.method == 'POST':
        itinerary.delete()
        return redirect('tours:tour_package_detail', pk=package.pk)
    return render(request, 'tours/itinerary_confirm_delete.html', {'itinerary': itinerary, 'package': package})