from import_export import resources

from ..models import DiaryEntry


class DiaryEntryResource(resources.ModelResource):
    """Resource class for ``DiaryEntry`` model."""

    class Meta:
        model = DiaryEntry
