from django.contrib import admin
from django.http.response import HttpResponseRedirect
from django.shortcuts import reverse
from django.utils.translation import ugettext_lazy as _

from django_object_actions import (
    DjangoObjectActions,
    takes_instance_or_queryset,
)


class BaseModelAdmin(DjangoObjectActions, admin.ModelAdmin):
    """Base model admin class."""

    url_index = None
    url_detail = None

    @takes_instance_or_queryset
    def on_site(self, request, qs=None):
        """View item on site."""
        if qs.count() > 1:
            return self.redirect(reverse(self.url_index))

        obj = qs.first()
        return self.redirect(reverse(self.url_detail, args=(obj.slug,)))

    on_site.label = _('View on site')

    @takes_instance_or_queryset
    def reset_slug(self, request, qs):
        """Reset `slug` field for object or queryset."""
        for obj in qs:
            obj.slug = None
            obj.save()

    reset_slug.label = _('Reset slug')

    def redirect(self, url):
        """Redirect user to provided URL."""
        return HttpResponseRedirect(url)
