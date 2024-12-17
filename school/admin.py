from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from school.models import School, Domain

@admin.register(School)
class SchoolAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = ('name',)


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'tenant', 'is_primary')
    list_filter = ('is_primary',)
    search_fields = ('domain', 'tenant__name')

