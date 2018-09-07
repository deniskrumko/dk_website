from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_color(dictionary, key):
    item = dictionary.get(key)
    return item.color if item else None


@register.filter
def get_name(dictionary, key):
    item = dictionary.get(key)
    return item.name if item else None


@register.filter
def get_link(dictionary, key):
    item = dictionary.get(key)
    return item.url if item else None
