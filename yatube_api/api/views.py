from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer
from posts.models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['partial_update', 'destroy']:
            return (IsAuthorOrReadOnly(),)
        return super().get_permissions()


class GroupViewSet:
    pass


class CommentViewSet:
    pass


class FollowViewSet:
    pass
