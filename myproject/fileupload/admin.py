from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import uFile

@admin.register(uFile)
class uFileAdmin(ImportExportModelAdmin):
    list_display = ('custState', 'dpd')