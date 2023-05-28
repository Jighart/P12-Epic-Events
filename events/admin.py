from django.contrib import admin

from events.models import Event
from users.models import SUPPORT


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Event Info",
            {
                "fields": (
                    "name",
                    "location",
                    "contract",
                    "attendees",
                    "event_date",
                    "event_status",
                )
            },
        ),
        ("Support", {"fields": ("support_contact", "notes")}),
        ("Info", {"fields": ("date_created", "date_updated")}),
    )
    readonly_fields = ("date_created", "date_updated")
    list_display = (
        "name",
        "location",
        "contract",
        "support_contact",
        "attendees",
        "event_date",
        "event_status",
    )
    list_filter = ("event_status", "support_contact")
    search_fields = ("name", "location", "client__last_name")

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request):
        try:
            if not request.user.team == SUPPORT:
                return False
            return True
        except AttributeError:
            pass

    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if obj:
            if not request.user.team == SUPPORT and not request.user.id == obj.support_contact:
                return False
        return True

    def has_change_permission(self, request, obj=None):
        if obj:
            if not request.user.team == SUPPORT and not request.user == obj.contract.sales_contact:
                print(obj.contract.sales_contact)
                return False
        return True
