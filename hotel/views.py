from django.shortcuts import get_object_or_404, render
from .models import Hotel
from datetime import datetime
from .froms import SearchForm



# Create your views here.

def home(request):
    hotels = Hotel.objects.all()
    return render(request,'hotel/home.html',  {'hotels': hotels})


def hotelList(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    return render(request, 'hotel/detail.html', {'hotel': hotel})


def test(request):
    return render(request, 'hotel/logout.html')


def hotel_search(request):
    # Handle both city, guest_count, and rating search parameters
    city = request.GET.get('city', '')
    guest_count = request.GET.get('guest_count', '')
    rating = request.GET.get('rating', 0)

    hotels = Hotel.objects.all()

    if city:
        hotels = hotels.filter(city__icontains=city)

    if guest_count:
        hotels = hotels.filter(guest_count__gte=guest_count)

    if rating:
        hotels = hotels.filter(rating__gte=rating)

    # Order hotels by rating in descending order
    hotels = hotels.order_by('-rating')

    # Handle date search
    form = SearchForm(request.GET)

    if form.is_valid():
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']

        # Filter available hotels based on the date range
        hotels = hotels.exclude(
            availability__start_date__lte=start_date, 
            availability__end_date__gte=end_date
        )

    return render(request, 'hotel/hotel_search.html', {'hotels': hotels, 'form': form})