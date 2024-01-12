from django.db import models

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
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def calculate_discounted_price(self):
        discount_amount = (self.discount_percentage / 100) * float(self.price)
        discounted_price = float(self.price) - discount_amount
        return round(discounted_price, 2)

    def __str__(self):
        return self.name
    
    
    