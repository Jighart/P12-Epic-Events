from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

from users.models import SALES, SUPPORT, MANAGEMENT
from contracts.models import Contract


class ContractPermissions(permissions.BasePermission):
    """
    Sales team : can CREATE new contracts
                 can VIEW and UPDATE contracts of their own clients
    Support team : can VIEW contracts of their own clients
    """

    def has_permission(self, request, view):
        if request.user.team == SUPPORT:
            return request.method in permissions.SAFE_METHODS
        return request.user.team in {SALES, MANAGEMENT}

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if request.user.team == SUPPORT:
                return obj in Contract.objects.filter(event__support_contact=request.user)
            return request.user == obj.sales_contact or request.user.team == MANAGEMENT
        elif request.method == "PUT" and obj.status is True:
            raise PermissionDenied("Cannot update a signed contract.")
        return request.user == (obj.sales_contact and obj.status is False) or request.user.team == MANAGEMENT
