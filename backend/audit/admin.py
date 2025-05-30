from django.contrib import admin
from .models import Audit, Incident

@admin.register(Audit)
class AuditAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'start_date', 'end_date', 'created_by')
    list_filter = ('status',)
    search_fields = ('title', 'description')

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('title', 'severity', 'reported_at', 'resolved', 'audit')
    list_filter = ('severity', 'resolved')
    search_fields = ('title', 'description')
