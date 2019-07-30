from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from core.admin import image_preview

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    """Admin class for ``User`` model."""

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Profile image'), {'fields': ('image', '_preview')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = (
        '_preview',
    )
    list_display = (
        'username',
        'email',
        '_preview',
        'is_staff',
        'is_superuser',
    )

    def _preview(self, obj):
        return image_preview(obj, size='large', field='image')

    _preview.short_description = _('Preview')
    _preview.admin_order_field = 'image'

    class Media:
        css = {
            'all': ('css/admin.css',)
        }
