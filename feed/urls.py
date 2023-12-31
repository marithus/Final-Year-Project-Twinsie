from . import views
from .views import AllSaveView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, SaveView, UserPostListView, LikeView,LikeCommentView, posts_of_following_profiles,  AllLikeView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', views.first, name='firsthome'),
    path('api/', include(router.urls)),
    path('home/', PostListView.as_view(), name='feed-home'),
    path('feed/', posts_of_following_profiles, name='posts-follow-view'),
    path('post/user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView, name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/like/', LikeView, name='post-like'),
    path('liked-posts/', AllLikeView, name='all-like'),
    path('post/save/', SaveView, name='post-save'),
    path('saved-posts/', AllSaveView, name='all-save'),
    path('post/comment/like/', LikeCommentView, name='comment-like'),
    path('about/', views.about, name='feed-about'),
    path('search/', views.search, name='search'),
]