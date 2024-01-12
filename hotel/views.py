from django.shortcuts import get_object_or_404, render
from .models import Hotel

# Create your views here.

def home(request):
    hotels = Hotel.objects.all()
    return render(request,'hotel/home.html',  {'hotels': hotels})


def hotelList(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    return render(request, 'hotel/detail.html', {'hotel': hotel})


def test(request):
    return render(request, 'hotel/logout.html')
