from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)


urlpatterns = [
    path('all/', views.ProfileListView.as_view(), name='profile-list-view'),
    path('api/', include(router.urls)),
    path('follow/', views.follow_unfollow_profile, name='follow-unfollow-view'),
    path('<int:pk>/', views.ProfileDetailView.as_view(), name='profile-detail-view'),
    path('public-profile/<str:username>/', views.public_profile, name='public-profile'),
    
]