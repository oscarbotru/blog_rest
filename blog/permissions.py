from rest_framework.permissions import BasePermission


class AuthorOrManager(BasePermission):

    def has_permission(self, request, view):
        if view.action in ['create', 'retrieve', 'update', 'partial_update', 'destroy']:
            return request.user.is_staff
        return True
