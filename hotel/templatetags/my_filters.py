from django import template
from datetime import datetime

register = template.Library()

@register.filter(name='has_overlap')
def has_overlap(availabilities, start_date, end_date):
    for availability in availabilities:
        if availability.start_date <= end_date and availability.end_date >= start_date:
            return True
    return False

register = template.Library()

@register.filter
def is_available(hotel, start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

    for availability in hotel.availability_set.all():
        if availability.start_date <= end_date and availability.end_date >= start_date:
            return True
    return False