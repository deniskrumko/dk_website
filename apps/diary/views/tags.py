from django.shortcuts import get_object_or_404

from ..models import DiaryTag, DiaryTagGroup
from .diary import BaseDiaryView

__all__ = (
    'DiaryTagsIndexView',
    'DiaryTagsDetailView',
    'DiaryEditGroupsView',
)


class DiaryTagsIndexView(BaseDiaryView):
    """View to get index page for diary tags."""

    template_name = 'diary/tags/index.html'
    title = 'DK - Тэги'
    description = 'Тэги дневника'

    def get_context_data(self):
        """Get context data."""
        context = super().get_context_data()
        context['groups'] = DiaryTagGroup.objects.filter(author=self.user)
        context['without_groups'] = DiaryTag.objects.filter(author=self.user, group__isnull=True)
        return context


class DiaryTagsDetailView(BaseDiaryView):
    """View to get single tag info."""

    template_name = 'diary/tags/detail.html'

    def get_title(self, **kwargs):
        """Get `title` field value."""
        item = kwargs.get('item')
        return f'DK - #{item.name}' if item else ''

    def get_description(self, **kwargs):
        """Get `description` field value."""
        item = kwargs.get('item')
        return item.name if item else ''

    def get(self, request, tag):
        """Get tag details."""
        item = get_object_or_404(DiaryTag, name=tag, author=self.user)
        years = item.entries.values_list(
            'date__year', flat=True,
        ).order_by('-date__year').distinct()
        context = self.get_context_data(item=item)
        context['tag'] = item
        context['stats'] = [('Всего', item.entries.count())] + [
            (year, item.entries.filter(date__year=year).count())
            for year in years
        ]
        return self.render_to_response(context)


class DiaryEditGroupsView(BaseDiaryView):
    """View to edit tags/tag groups."""

    template_name = 'diary/tags/edit_groups.html'
    title = 'DK - Редактировать группы'

    def get(self, request):
        """Get tag groups."""
        context = self.get_context_data()
        context['groups'] = DiaryTagGroup.objects.filter(author=self.user)
        context['tags'] = DiaryTag.objects.filter(author=self.user)
        return self.render_to_response(context)

    def post(self, request):
        """Create/update/delete tag groups."""
        data = self.request.POST

        if 'save_groups' in data:
            for group in DiaryTagGroup.objects.filter(author=self.user):
                to_delete = data.get(f'group__{group.id}__delete')
                if to_delete:
                    group.delete()
                    continue

                group.name = data.get(f'group__{group.id}__name')
                group.color = data.get(f'group__{group.id}__color')
                group.order = data.get(f'group__{group.id}__order')
                group.save()

            new_groups = data.get('new_groups')
            if new_groups:
                for new_group in new_groups.split(','):
                    DiaryTagGroup.objects.get_or_create(
                        author=self.user,
                        name=new_group.strip(),
                    )

        if 'save_tags' in data:
            for tag in DiaryTag.objects.filter(author=self.user):
                new_value = data.get(f'tag__{tag.id}')
                if tag.group and not new_value:
                    tag.group = None
                    tag.save()

                if new_value:
                    tag.group = DiaryTagGroup.objects.filter(author=self.user, id=new_value).first()
                    tag.save()

        return self.redirect('diary:edit_groups')
