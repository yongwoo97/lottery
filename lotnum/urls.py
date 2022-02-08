from django.urls import path, include
from .views import GetNum

urlpatterns = [
    path('<int:pk>/', GetNum),
]