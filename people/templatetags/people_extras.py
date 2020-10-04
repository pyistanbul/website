from django import template
from django.utils.safestring import mark_safe

register = template.Library()


def fontawesome(icon_name, size=""):
    """
    Generate fontawesome syntax for HTML.

    Usage:

        {% fontawesome "iconname" %}
        {% fontawesome "iconname" "size" %}

    Size values are: lg, 2x, 3x, 4x, 5x
    """
    if len(size) > 0:
        size = "fa-%s" % size
    result = '<i class="fa fa-%s %s"></i>' % (icon_name, size)
    return mark_safe(result)


register.simple_tag(fontawesome)
