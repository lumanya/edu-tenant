from django.shortcuts import render, redirect
from django_tenants.utils import schema_context
from django.contrib.auth import login
from django.conf import settings
from tenant_manager.models import Tenant, Domain, TenantMember
from django.contrib import messages
from .forms import TenantForm
from schools.models import Student
from django.contrib.auth.decorators import login_required


@login_required
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
            
            messages.success(request, 'School Registered successfull!')       

            return redirect(f"http://{domain.domain}{settings.PORT}")
        else:
            print('the form has not been create')
            tenant = None
    
    
    if not hasattr(request, 'tenant'):
        template_name = 'home.html'
    else:
        template_name = 'home_tenant.html'
    
    students = Student.objects.all()    

    context = {
        'tenant_form': tenant_form,
        'students': students
        
       
        }

    return render(request, template_name, context)


@login_required
def  school_directory_page(request):
    # list all tenants
    tenant = Domain.objects.all()
    
    print(tenant)
    contex = {
        'schools': tenant
    }
    return render(request, 'schools.html', contex)
    
    
