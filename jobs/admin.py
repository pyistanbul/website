from copy import deepcopy

from django.contrib import admin

from jobs.models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('title', 'company', 'location'),
        }),
        ('Detay Bilgiler', {
            'fields': ('is_expired', 'url', 'date_created', 'description'),
        }),
    )

    list_display = ('title', 'company', 'is_expired')
    list_filter = ('is_expired', 'company')
    search_fields = ('title', 'company')

    def has_add_permission(self, request):
        return False
