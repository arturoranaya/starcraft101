from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class EntradaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre', 'liga_main', 'tut_from']
    list_display = ('nombre', 'match', 'liga_main', 'tut_from', 'estado')


admin.site.register(Entrada, EntradaAdmin)
