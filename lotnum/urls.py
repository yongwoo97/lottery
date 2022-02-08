from django.urls import path, include
from .views import num

urlpatterns = [
    path('', num),
]