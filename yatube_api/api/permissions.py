from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    """Даем разрешение на чтение всем,
    а изменение только если пользователь автор объекта.
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )


class UserIsAuthAndGetPost(permissions.BasePermission):
    """Даем права доступа только аутентифицированным
    пользователям и только GET и POST.
    """

    def has_permission(self, request, view):
        return (
            request.method in ['POST', 'GET']
            and request.user.is_authenticated
        )


class GroupReadOnlyForAll(permissions.BasePermission):
    """Даем возможность всем делать запросы на чтение"""

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS
