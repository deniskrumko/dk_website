from core.admin import BaseModelForm

from .models import VideoFile


class VideoFileForm(BaseModelForm):
    """Form for ``VideoFileAdmin`` class."""

    class Meta:
        model = VideoFile
        fields = '__all__'
        widgets = {
            'name': BaseModelForm.input_widget(),
            'source_1080': BaseModelForm.text_widget(),
            'source_720': BaseModelForm.text_widget(),
            'source_480': BaseModelForm.text_widget(),
            'source_360': BaseModelForm.text_widget(),
            'youtube_link': BaseModelForm.text_widget(),
        }
