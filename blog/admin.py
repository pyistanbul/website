from django.contrib import admin
from .models import Post


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_published",)
    list_filter = ('is_published',)
    search_fields = ("title", "slug", "description",)

admin.site.register(Post, BlogAdmin)
