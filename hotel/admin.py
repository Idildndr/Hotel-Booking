from django.contrib import admin
from .models import Hotel, Amenity,Availability, AvailabilityAdmin

# Register the models with their respective admins
admin.site.register(Amenity)
admin.site.register(Hotel)
admin.site.register(Availability)  # Register the Availability model

