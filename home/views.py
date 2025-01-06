from django.shortcuts import render, redirect
from django_tenants.utils import schema_context
from django.contrib.auth import login
from django.conf import settings
from tenant_manager.models import Tenant, Domain, TenantMember
from .forms import TenantForm


def home_view(request):
    tenant_form = TenantForm()

    if request.method == 'POST':
        tenant_form = TenantForm(request.POST)
        if tenant_form.is_valid():
            tenant = tenant_form.save()

            domain = Domain.objects.create(
                tenant=tenant,
                domain=f"{tenant.schema_name}.{settings.BASE_URL}",
                is_primary=True
            )

            TenantMember.objects.create(
                user=request.user,
                tenant=tenant,
                is_admin=True
            )
       

            return redirect(f"http://{domain.domain}{settings.PORT}")
        else:
            tenant = None
    
    
    if not hasattr(request, 'tenant'):
        template_name = 'home.html'
    else:
        template_name = 'home_tenant.html'
    

    context = {
        'tenant_form': tenant_form,
       
        }

    return render(request, template_name, context)
