from django.urls import path, include
from .views import num, nums

urlpatterns = [
    path('', num),
    path('second/', nums),
]