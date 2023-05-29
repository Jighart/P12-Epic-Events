from rest_framework import permissions

from users.models import SALES, SUPPORT, MANAGEMENT
from clients.models import Client


class ClientPermissions(permissions.BasePermission):
    """
    Sales team : can CREATE new clients
                 can VIEW clients
                 can UPDATE any prospect and their own clients
                 can DELETE prospects only
    Support team : can VIEW clients
    """

    def has_permission(self, request, view):
        if request.user.team == SUPPORT:
            return request.method in permissions.SAFE_METHODS
        return request.user.team in {SALES, MANAGEMENT}

    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE":
            return request.user.team in {SALES, MANAGEMENT} and obj.status is False
        elif request.user.team == SUPPORT:
            return request.method in permissions.SAFE_METHODS
        return request.user == obj.sales_contact or obj.status is False or request.user.team == MANAGEMENT
