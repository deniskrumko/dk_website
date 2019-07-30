from django.contrib.sitemaps import GenericSitemap, Sitemap

from apps.blog.models import BlogEntry
from apps.music.models import Track

__all__ = ('config',)


class IndexPagesSitemap(Sitemap):
    """Sitemap for index pages."""
    priority = 1
    changefreq = 'daily'

    def items(self):
        return ['/', '/blog', '/music']

    def location(self, item):
        return item


config = {
    'index': IndexPagesSitemap,
    'blog': GenericSitemap({
        'queryset': BlogEntry.objects.all(),
        'date_field': 'modified',
    }),
    'music': GenericSitemap({
        'queryset': Track.objects.all(),
        'date_field': 'modified',
    }),
}
