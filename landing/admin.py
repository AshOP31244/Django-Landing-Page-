from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        "company_name",
        "contact_person",
        "phone",
        "email",
        "capacity",
        "created_at",
    )
