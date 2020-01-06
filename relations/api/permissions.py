from rest_framework import permissions
from core.models import Blacklist


class BlacklistPermission(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """

    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
        return not blacklisted


class AnonPermissionOnly(permissions.BasePermission):
    """
    Permissions for non-logged in users for browsing the website, viewing examples, registering etc.
    """

    def has_permission(self, request, view):
        message = "Sorry you are already logged in! Please logout and try again"
        return not request.user.is_authenticated


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object level permission to only allow owners of an object to view / edit it
    Assumes the model has an 'owner' attribute
    """
    message = "You do not have permissions to make this change"
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
