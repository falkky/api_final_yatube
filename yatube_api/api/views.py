from rest_framework import mixins
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from .permissions import AuthorOrReadOnly, GroupReadOnlyForAll
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer
)
from posts.models import Group, Post


class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    """Кастомный класс который предоставляет
    действия `retrieve`, `create`, `list`
    """
    pass


class PostViewSet(viewsets.ModelViewSet):
    """Представление для запросов к постам."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Метод получает автора из запроса и сохраняет пост"""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Представление для запросов к группам, только чтение."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (GroupReadOnlyForAll,)


class CommentViewSet(viewsets.ModelViewSet):
    """Представление для запросов к комментариям."""
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        """Метод получает id поста из запроса
        и возвращает комментарии к нему.
        """
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        """Метод получает id поста и пользователя из запроса,
        и создает комментарий к посту.
        """
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(CreateListRetrieveViewSet):
    """Представление для запросов к подпискам."""
    serializer_class = FollowSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        """Метод возвращает все подписки пользователя."""
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        """Метод получает из запроса пользователя
        и создает подписку на другого пользователя.
        """
        serializer.save(user=self.request.user)
