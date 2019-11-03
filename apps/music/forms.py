from django import forms

from core.utils import time_int_to_str, time_str_to_int

from . import models


class DurationWidget(forms.TextInput):
    """Widget for `duration` field."""

    def format_value(self, value):
        """Format value.

        Return a value as it should appear when rendered in a template.

        """
        return time_int_to_str(value)

    def value_from_datadict(self, data, files, name):
        """Get value.

        Given a dictionary of data and this widget's name, return the value
        of this widget or None if it's not provided.

        """
        value = data.get(name)
        return time_str_to_int(value)


class TrackForm(forms.ModelForm):
    """Form for ``TrackAdmin`` class."""

    class Meta:
        model = models.Track
        fields = '__all__'
        widgets = {
            'duration': DurationWidget(),
        }
