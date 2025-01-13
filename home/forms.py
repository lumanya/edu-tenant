from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
import re
from tenant_manager.models import Tenant, Domain


class TenantForm(ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'schema_name', 'address']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'School Name..',
                'class': 'w-full p-2 border-4 border-rose-600 rounded-lg focus:ring-red-500 focus:border-sky-500 shadow-sm'
            }),
            'schema_name': forms.TextInput(attrs={
                'placeholder': 'Add Subdomain..',
                'class': 'w-full p-2 border border-sky-300 rounded-lg focus:ring-sky-500 focus:border-sky-500'
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'Address',
                'class': 'w-full p-2 border border-sky-300 rounded-lg focus:ring-sky-500 focus:border-sky-500'
            }),
        }
        labels = {
            'name': '',
            'schema_name': '',
            'address': '',
        }

    def clean_schema_name(self):
        schema_name = self.cleaned_data['schema_name'].lower() 

        if not re.match(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', schema_name):
            raise ValidationError("Subdomains can only contain lowercase letters, numbers, and hyphens!")
        
        if Tenant.objects.filter(schema_name=schema_name).exists():
            raise ValidationError("This subdomain is already taken.")
        
        return schema_name