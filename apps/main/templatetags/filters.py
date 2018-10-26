from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    """Get `item` field value."""
    return dictionary.get(key)


@register.filter
def get_color(dictionary, key):
    """Get `color` field value."""
    item = dictionary.get(key)
    return item.color if item else None


@register.filter
def get_name(dictionary, key):
    """Get `name` field value."""
    item = dictionary.get(key)
    return item.name if item else None


@register.filter
def get_link(dictionary, key):
    """Get `link` field value."""
    item = dictionary.get(key)
    return item.url if item else None
