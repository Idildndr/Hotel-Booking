from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name= "home"),
    path('hotels/<int:hotel_id>/', views.hotelList, name='detail'),
    path('test/',views.test,name='test')

    
]


