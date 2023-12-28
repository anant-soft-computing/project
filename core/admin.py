from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Event, Registration


@admin.register(Registration)
class RegistrationAdmin(ImportExportModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    pass
