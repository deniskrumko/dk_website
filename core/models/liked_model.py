from django.db import models
from django.utils.translation import ugettext_lazy as _

LIKED_MODELS_REGISTRY = {}


class LikedModel(models.Model):
    likes_counter = models.PositiveIntegerField(
        null=True,
        default=0,
        verbose_name=_('likes counter'),
    )

    class Meta:
        abstract = True

    def increment_likes(self):
        self.likes_counter += 1
        self.save()
        return self.likes_counter


def register_liked_model(name):
    def inner(cls):
        assert LIKED_MODELS_REGISTRY.get(name) is None
        LIKED_MODELS_REGISTRY[name] = cls
        cls.likes_name = name
        return cls
    return inner
