from django.conf import settings


def export_blog_settings(request):
    return {
        'BLOG_SETTINGS': settings.BLOG
    }
