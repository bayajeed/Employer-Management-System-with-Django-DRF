from django.contrib import admin
from .models import Employer

@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contact_person_name', 'email', 'user')
    list_filter = ('user',)
    search_fields = ('company_name', 'contact_person_name', 'email')
    raw_id_fields = ('user',)