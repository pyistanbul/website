from django import template

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
    return '<i class="fa fa-%s %s"></i>' % (icon_name, size)


register.simple_tag(fontawesome)
