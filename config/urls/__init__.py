from django.urls import path
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

admin.site.site_header = _('Denis Krumko')
admin.site.site_title = _('DK')

urlpatterns = [
    path('admin/', admin.site.urls),
]
