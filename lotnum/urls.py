from django.urls import path, include
from .views import GetNum, num

urlpatterns = [
    path('', num),
    path('<int:pk>/', GetNum),
]