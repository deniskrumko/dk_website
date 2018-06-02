from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_color(dictionary, key):
    return dictionary.get(key).color


@register.filter
def get_name(dictionary, key):
    return dictionary.get(key).name
