from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.utils.translation import ugettext_lazy as _

from . import sitemaps

admin.site.site_header = _('Denis Krumko')
admin.site.site_title = _('DK')

urlpatterns = [
    # Apps
    path('', include('apps.main.urls', namespace='main')),
    path('blog/', include('apps.blog.urls', namespace='blog')),
    path('music/', include('apps.music.urls', namespace='music')),
    path('diary/', include('apps.diary.urls', namespace='diary')),
    path('news/', include('apps.news.urls', namespace='news')),

    # Admin UI
    path('admin/', admin.site.urls),

    # Users
    path('', include('apps.users.urls', namespace='users')),

    # Sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps.config},
         name='django.contrib.sitemaps.views.sitemap'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
