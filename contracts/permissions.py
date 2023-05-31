from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

from users.models import SALES, SUPPORT, MANAGEMENT


class ContractPermissions(permissions.BasePermission):
    """
    Sales team : can CREATE new contracts
                 can VIEW contracts
                 can UPDATE contracts of their own clients
                 can DELETE unsigned contracts of their own clients
    Support team : can VIEW contracts
    """

    def has_permission(self, request, view):
        if request.user.team == SUPPORT:
            return request.method in permissions.SAFE_METHODS
        return request.user.team in {SALES, MANAGEMENT}

    def has_object_permission(self, request, view, obj):
        if request.user.team == SUPPORT:
            return request.method in permissions.SAFE_METHODS
        elif request.method == 'DELETE' and obj.status.name == 'SIGNED':
            raise PermissionDenied('Cannot delete a signed contract.')
        return request.user == obj.sales_contact or request.user.team == MANAGEMENT
