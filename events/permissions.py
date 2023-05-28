from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

from users.models import SALES, SUPPORT, MANAGEMENT


class EventPermissions(permissions.BasePermission):
    """
    Sales team : can CREATE new events
                 can VIEW events of their own clients
                 can UPDATE events of their own clients if not finished
    Support team : can VIEW events of their own clients
                   can UPDATE events of their own clients if not finished
    """

    def has_permission(self, request, view):
        if request.user.team == SUPPORT:
            return request.method in ["GET", "PUT"]
        return request.user.team in {SALES, MANAGEMENT}

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user in {obj.support_contact, obj.contract.sales_contact}
        else:
            if obj.event.status.name == 'COMPLETE':
                raise PermissionDenied("Cannot update a finished event.")
            if request.user.team == SUPPORT:
                return request.user == obj.support_contact
            return request.user == obj.contract.sales_contact or request.user.team == MANAGEMENT
