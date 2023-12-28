from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Event, Registration


@admin.register(Registration)
class RegistrationAdmin(ImportExportModelAdmin):
    list_display = ["id", "name", "category", "batch_year", "mobile_no", "tshirt_size"]
    list_filter = ["category", "batch_year", "tshirt_size", "id"]

    list_per_page = 20


@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    pass
