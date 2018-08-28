from django.contrib import admin
from django.http.response import HttpResponseRedirect
from django.shortcuts import reverse
from django.utils.translation import ugettext_lazy as _

from django_object_actions import (
    DjangoObjectActions,
    takes_instance_or_queryset,
)


class BaseModelAdmin(DjangoObjectActions, admin.ModelAdmin):

    @takes_instance_or_queryset
    def on_site(self, request, qs=None):
        """Method to view tracks or one track on site."""
        if qs.count() > 1:
            return HttpResponseRedirect(reverse(self.url_index))

        obj = qs.first()
        return HttpResponseRedirect(reverse(self.url_detail, args=(obj.slug,)))

    on_site.label = _('View on site')

    @takes_instance_or_queryset
    def reset_slug(self, request, qs):
        """Action to reset `slug` field for ``Track`` objects."""
        for obj in qs:
            obj.slug = None
            obj.save()

    reset_slug.label = _('Reset slug')
