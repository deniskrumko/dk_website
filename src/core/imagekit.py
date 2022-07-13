class ImageKitCacheFile:
    """Custom class for image kit caching.

    Source:
    https://github.com/matthewwithanm/django-imagekit/issues/391

    """

    def on_content_required(self, file):
        """Get `on_content_required` field value."""
        try:
            file.generate()
        except Exception:
            pass

    def on_existence_required(self, file):
        """Get `on_existence_required` field value."""
        try:
            file.generate()
        except Exception:
            pass
