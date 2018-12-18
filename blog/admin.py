from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Post


class BlogAdmin(MarkdownxModelAdmin):
    list_display = ("title", "slug", "is_published",)
    list_filter = ('is_published',)
    search_fields = ("title", "slug", "description",)
    exclude = ("author",)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(Post, BlogAdmin)
