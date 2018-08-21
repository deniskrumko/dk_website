from django.urls import path, include
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

admin.site.site_header = _('Denis Krumko')
admin.site.site_title = _('DK')

urlpatterns = [
    # Apps
    path('', include('apps.main.urls', namespace='main')),
    path('blog/', include('apps.blog.urls', namespace='blog')),
    path('music/', include('apps.music.urls', namespace='music')),
    path('diary/', include('apps.diary.urls', namespace='diary')),

    # Admin UI
    path('admin/', admin.site.urls),

    # Users
    path('', include('apps.users.urls', namespace='users')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
