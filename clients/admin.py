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

    def has_module_permission(self, request):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if obj:
            if request.user.team not in {SALES, MANAGEMENT} and not request.user.id == obj.sales_contact:
                return False
        return True

    def has_change_permission(self, request, obj=None):
        if obj:
            if request.user.team not in {SALES, MANAGEMENT} and not request.user.id == obj.sales_contact:
                return False
        return True

    def has_add_permission(self, request):
        try:
            if request.user.team in {SALES, MANAGEMENT}:
                return True
            return False
        except AttributeError:
            pass
