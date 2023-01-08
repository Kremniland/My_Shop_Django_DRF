from django.urls import path
from .views import get_index


urlpatterns = [
    path('', get_index, name='home'),
]