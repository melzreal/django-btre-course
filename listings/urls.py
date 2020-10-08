from django.urls import path

from . import views

# when inside the listings app, the '' path will pertain to /listings
# when you want a parameter to add the id, add <> and the type of parameter
# use the main urls file to tell the main app that anything with /listings prepended should direct here path('listings/', include('listings.urls')),
# use the main settings file to tell the main app this app exists by adding 'listings.apps.ListingsConfig' to the INSTALLED_APPS

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='listing'),
]
