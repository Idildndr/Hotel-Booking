from datetime import datetime
from django import forms, template

class HotelSearchForm(forms.Form):
    city = forms.CharField(required=False)
    guest_count = forms.IntegerField(required=False)
    order_by_rating = forms.BooleanField(required=False)
    
    
class SearchForm(forms.Form):
    start_date = forms.DateField(
        label='Start Date', 
        widget=forms.TextInput(attrs={'class': 'datepicker'}),
    )
    end_date = forms.DateField(
        label='End Date', 
        widget=forms.TextInput(attrs={'class': 'datepicker'}),
    )
    
