from django.urls import path
from . import views

app_name = 'tours'

urlpatterns = [
    path('', views.tour_package_list, name='tour_package_list'),
    path('package/create/', views.tour_package_create, name='tour_package_create'),
    path('package/<int:pk>/', views.tour_package_detail, name='tour_package_detail'),
    path('package/<int:pk>/update/', views.tour_package_update, name='tour_package_update'),
    path('package/<int:pk>/delete/', views.tour_package_delete, name='tour_package_delete'),

    path('package/<int:package_pk>/itinerary/add/', views.itinerary_create, name='itinerary_create'),
    path('itinerary/<int:pk>/update/', views.itinerary_update, name='itinerary_update'),
    path('itinerary/<int:pk>/delete/', views.itinerary_delete, name='itinerary_delete'),
]