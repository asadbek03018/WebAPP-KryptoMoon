from django.urls import path
from .views import exchanger

urlpatterns = [
    path('exchange/', exchanger, name='exchange')
]