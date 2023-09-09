from notification.views import ShowNotifications
from django.urls import path, include
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', ShowNotifications, name='show-notifications'),
]