from django.contrib import admin

from .models import Tenant, Domain, TenantMember


class TenantAdminSite(admin.AdminSite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register(Tenant)
        self.register(Domain)
        self.register(TenantMember)


tenant_admin_site = TenantAdminSite(name="tenant_admin_site")