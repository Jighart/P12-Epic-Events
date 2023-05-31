from django.contrib import admin

from .models import Client
from users.models import SALES, MANAGEMENT


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Client/Prospect Info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "company_name",
                    "email",
                    "phone",
                    "mobile",
                )
            },
        ),
        ("Sales", {"fields": ("status", "sales_contact")}),
        ("Info", {"fields": ("date_created", "date_updated")}),
    )
    list_display = (
        "full_name",
        "company_name",
        "email",
        "phone",
        "mobile",
        "status",
        "sales_contact",
    )
    list_filter = ("status", "sales_contact")
    search_fields = ("first_name", "last_name", "company_name", "sales_contact")
    readonly_fields = ("date_created", "date_updated")

    @staticmethod
    def full_name(obj):
        return f"{obj.first_name} {obj.last_name}"

    # Permissions
    #
    # Sales team : can CREATE new clients
    #              can VIEW clients
    #              can UPDATE any prospect and their own clients
    #              can DELETE prospects only
    # Support team : can VIEW clients

    def has_module_permission(self, request):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return request.user.is_authenticated and request.user.team in {SALES, MANAGEMENT}

    def has_change_permission(self, request, obj=None):
        if obj:
            return (request.user == obj.sales_contact and obj.status is False) or request.user.team == MANAGEMENT

    def has_delete_permission(self, request, obj=None):
        if obj:
            if request.user == obj.sales_contact or request.user.team == MANAGEMENT:
                return not obj.status
            return False
