from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        #if the request.method is GET,OPTION or HEAD, provide the permission
        if request.method in  permissions.SAFE_METHODS:
            return True
        return request.user == obj.owner