from django import forms


class BaseModelForm(forms.ModelForm):
    """Base ``ModelForm`` class."""

    @classmethod
    def width_attr(cls, pixels, full_width=False):
        """Class method to get width attributes."""
        width = 'width: 100%;' if full_width else ''
        return {'attrs': {'style': f'max-width: {pixels}px;{width}'}}

    @classmethod
    def text_widget(cls, max_width=600, rows=2):
        """Class method to get widget for ``TextField``."""
        return forms.Textarea(attrs={
            'style': f'max-width: {max_width}px; width: 100%;', 'rows': rows,
        })

    @classmethod
    def input_widget(cls, max_width=600, full_width=True):
        """Class method to get widget for ``CharField``."""
        return forms.TextInput(**cls.width_attr(max_width, full_width))
