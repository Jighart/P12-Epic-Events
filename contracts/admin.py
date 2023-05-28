from django.contrib import admin

from contracts.models import Contract
from users.models import SALES


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Contract Info", {"fields": ("client", "amount", "payment_due")}),
        ("Sales", {"fields": ("status", "sales_contact")}),
        ("Info", {"fields": ("date_created", "date_updated")}),
    )
    readonly_fields = ("date_created", "date_updated")
    list_display = (
        "contract_number",
        "sales_contact",
        "client",
        "amount",
        "payment_due",
        "status",
    )
    list_filter = ("status", "sales_contact")
    search_fields = ("contract_number", "client__last_name")

    @staticmethod
    def contract_number(obj):
        return f"Contract #{obj.id}"

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request):
        try:
            if not request.user.team == SALES:
                return False
            return True
        except AttributeError:
            pass

    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if obj:
            if not request.user.team == SALES and not request.user.id == obj.sales_contact:
                return False
        return True

    def has_change_permission(self, request, obj=None):
        if obj:
            if not request.user.team == SALES and not request.user.id == obj.sales_contact:
                return False
        return True
