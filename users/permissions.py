from rest_framework import permissions


class IsOwnerPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.username == obj.username:
            return True
        return False
