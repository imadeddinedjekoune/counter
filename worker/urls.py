from django.urls import path
from .views import hello_world , counter_value
 
urlpatterns = [
    path('', hello_world),
    path('counter/', counter_value, name='counter-value')
]