from django.contrib import admin

from events.models import Event
from users.models import SALES, MANAGEMENT


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

    # Permissions
    #
    # Sales team : can CREATE new events
    #              can VIEW events
    #              can UPDATE events of their own clients if not finished
    # Support team : can VIEW events
    #                can UPDATE events of their own clients if not finished

    def has_module_permission(self, request):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return request.user.is_authenticated and request.user.team in {SALES, MANAGEMENT}

    def has_change_permission(self, request, obj=None):
        if obj:
            if request.user.team == MANAGEMENT:
                return True
            elif request.user in {obj.contract.sales_contact, obj.support_contact}:
                return not obj.event_status.name == 'COMPLETE'
            return False

    def has_delete_permission(self, request, obj=None):
        if obj:
            return request.user.team == MANAGEMENT
