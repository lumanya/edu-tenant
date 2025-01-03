from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    registration_number = models.CharField()
    school_type = models.CharField()
    address = models.CharField()
    phone = models.CharField()
    created_on = models.DateField(auto_now_add=True)
    auto_create_schema = True


class Domain(DomainMixin):
    pass
