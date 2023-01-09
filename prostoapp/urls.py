from django.urls import path
from .views import get_index


app_name = 'prostoapp'

urlpatterns = [
    path('', get_index, name='home'),
]

