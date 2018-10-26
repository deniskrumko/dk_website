from django.utils.safestring import mark_safe


def image_preview(obj, size, field='image',):
    """Get image preview."""
    assert size in ('small', 'large')

    image_field = getattr(obj, field)
    return mark_safe(
        f'<a href="{image_field.url}" target="_blank">'
        f'<img src="{image_field.url}" class="{size}-preview">'
        f'</a>'
    ) if image_field else '-'
