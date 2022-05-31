from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    """Даем разрешение на чтение всем,
     а изменение только если пользователь автор объекта
     """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
