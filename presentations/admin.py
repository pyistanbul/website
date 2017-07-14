from django.contrib import admin

from .models import Presentation, PresentationRequest

class PresentationRequestAdmin(admin.ModelAdmin):
    model = PresentationRequest
    search_fields = ('presentation_title', 'presenter_name', )
    list_display = ('presentation_title', 'presenter_name', 'is_approved',
                    'is_reviewed', )
    list_filter = ('is_approved', 'is_reviewed', )


admin.site.register(Presentation)
admin.site.register(PresentationRequest, PresentationRequestAdmin)
