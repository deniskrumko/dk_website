from django.urls import path, include
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.views.generic.base import TemplateView
from django.conf import settings

from django.conf.urls.static import static

admin.site.site_header = _('Denis Krumko')
admin.site.site_title = _('DK')

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),

    path('music/', include('apps.music.urls', namespace='music')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
