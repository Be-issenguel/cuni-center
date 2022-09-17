from django.urls import path
from .views import library_index

urlpatterns = [
    path('', library_index, name='home'),
]
