from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FollowViewSet, CommentViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(
     r'posts/(?P<post_id>\d+)/comments',
     CommentViewSet,
     basename='comments')
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
