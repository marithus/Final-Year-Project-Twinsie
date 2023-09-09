from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'rooms', RoomViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', views.room_enroll, name='room-enroll'),
    path('api/', include(router.urls)),
    path('chat/<int:friend_id>', views.room_choice, name='room-choice'),
    path('room/<int:room_name>-<int:friend_id>', views.room, name='room'),
]