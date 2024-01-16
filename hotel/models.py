from decimal import Decimal, ROUND_HALF_UP
from django.db import models
from django.contrib import admin

class Amenity(models.Model):
    name = models.CharField(max_length=255)
    icon_url = models.ImageField(upload_to='icon_pictures/', blank=True, null=True)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    rating = models.FloatField()
    description = models.TextField(default="No description available")  # Set your default value here
    number_of_comments = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='hotel_pictures/', blank=True, null=True)
    amenities = models.ManyToManyField(Amenity)
    city = models.CharField(max_length=100)
    guest_count = models.IntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    has_discount = models.BooleanField(default=False)
    discount_rate = models.IntegerField(default=0)

    def calculate_discounted_price(self):
        if self.has_discount:
            discount_amount = self.discount_rate * self.price / 100
            discounted_price = self.price - discount_amount
            return discounted_price.quantize(Decimal('0.000'), rounding=ROUND_HALF_UP)
        else:
            return self.price


    def calculate_member_price(self):
        discount_percentage = Decimal('10')
        price = Decimal(self.price)
        discount_amount = (discount_percentage / Decimal('100')) * price
        discounted_price = price - discount_amount
        rounded_price = discounted_price.quantize(Decimal('0.000'), rounding=ROUND_HALF_UP)
        return rounded_price
    
    
    def __str__(self):
        return self.name
    
class Availability(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.hotel.name} - {self.start_date} to {self.end_date}"
    
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'formatted_start_date', 'formatted_end_date')

    def formatted_start_date(self, obj):
        return obj.start_date.strftime('%d.%m.%Y')

    def formatted_end_date(self, obj):
        return obj.end_date.strftime('%d.%m.%Y')

    formatted_start_date.short_description = 'Start Date'
    formatted_end_date.short_description = 'End Date'



# Register the modified AvailabilityAdmin
