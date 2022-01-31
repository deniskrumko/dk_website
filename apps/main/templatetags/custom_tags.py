from django import template

from core.utils import ru_date_format

register = template.Library()


@register.filter(name='rdate')
def ru_date_format_template_tag(date, format_str):
    """Add russian tags to date formatting."""
    return ru_date_format(date, format_str)
