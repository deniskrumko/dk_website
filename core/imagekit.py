class FixJustInTime:
    """
    Source:
    https://github.com/matthewwithanm/django-imagekit/issues/391
    """

    def on_content_required(self, file):
        try:
            file.generate()
        except Exception:
            pass

    def on_existence_required(self, file):
        try:
            file.generate()
        except Exception:
            pass
