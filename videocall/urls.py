from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomMemberViewSet

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'roommembers', RoomMemberViewSet)


urlpatterns = [
    path('', views.lobby, name='vc-lobby'),
    path('api/', include(router.urls)),
    path('room/', views.room, name='vc-room'),
    path('get_token/', views.getToken),

    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
]