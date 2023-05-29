from django.contrib import admin

from contracts.models import Contract
from users.models import SALES, MANAGEMENT


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

    # Permissions
    #
    # Sales team : can CREATE new contracts
    #              can VIEW contracts
    #              can UPDATE contracts of their own clients
    #              can DELETE unsigned contracts of their own clients
    # Support team : can VIEW contracts

    def has_module_permission(self, request):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        try:
            if request.user.team in {SALES, MANAGEMENT}:
                return True
            return False
        except AttributeError:
            pass

    def has_change_permission(self, request, obj=None):
        if obj:
            if request.user.team == MANAGEMENT or request.user == obj.sales_contact:
                return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj:
            if request.user.team == MANAGEMENT or request.user == obj.sales_contact:
                return not obj.status.name == 'SIGNED'
        return False
