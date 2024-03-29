from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Event, EventRegistration, Registration

# anubhuti events= "Anubhooti"


class EventRegistrationInline(admin.TabularInline):
    model = EventRegistration
    min_num = 1
    extra = 1
    fk_name = "registration"
    readonly_fields = ["present"]

@admin.register(Registration)
class RegistrationAdmin(ImportExportModelAdmin):
    ordering = ["-date_created"]
    date_hierarchy = "date_created"
    inlines = [EventRegistrationInline]
    list_display = [
        "id",
        "name",
        "category",
        "batch_year",
        "mobile_no",
        "tshirt_size",
        "barcode",
        "date_created",
        "date_updated",
    ]
    list_filter = [
        "id",
        "category",
        "batch_year",
        "tshirt_size",
    ]
    list_per_page = 20
    readonly_fields = [
        "barcode",
    ]

@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    list_display = [
        "event_name",
        "event_start_date",
        "event_end_date",
        "event_start_time",
        "event_end_time",
        "event_location",
    ]

@admin.register(EventRegistration)
class EventRegistrationAdmin(ImportExportModelAdmin):
    list_display = [
        "event",
        "registration",
        "present",
        "can_attend_multiple",
    ]

    list_filter = ["registration__name", "event", "present", "can_attend_multiple"]