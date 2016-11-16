from django.contrib import admin

from jobs.models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('title', 'company', 'location'),
        }),
        ('Detay Bilgiler', {
            'fields': ('url', 'date_created', 'description'),
        }),
    )

    list_display = ('title', 'company')
    list_filter = ('company',)
    search_fields = ('title', 'company')
