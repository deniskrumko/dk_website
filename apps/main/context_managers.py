from django.contrib.auth.models import Group
from django.shortcuts import reverse

from apps.blog.models import BlogEntry, BlogSeries
from apps.diary.models import DiaryEntry, DiaryTag, DiaryTagValue
from apps.files.models import File, FileCategory, VideoFile
from apps.main.models import RedirectPage, Tag
from apps.music.models import Album, Track
from apps.users.models import User


def admin_items(*items):
    def create_dict(model):
        name = model._meta.verbose_name_plural
        return {
            'name': name[0].upper() + name[1:],
            'url': reverse(
                'admin:{meta.app_label}_{meta.model_name}_changelist'
                .format(meta=model._meta)
            )
        }

    return [create_dict(item) for item in items]


def custom_admin(request):
    return {
        'left_menu': [
            {
                'title': 'Блог',
                'url': '/admin/blog/',
                'items': admin_items(BlogSeries, BlogEntry),
            },
            {
                'title': 'Музыка',
                'url': '/admin/music/',
                'items': admin_items(Track, Album),
            },
            {
                'title': 'Дневник',
                'url': '/admin/diary/',
                'items': admin_items(DiaryEntry, DiaryTag, DiaryTagValue),
            },
            {
                'title': 'Файлы',
                'url': '/admin/files/',
                'items': admin_items(File, VideoFile, FileCategory),
            },
            {
                'title': 'Пользователи',
                'url': '/admin/auth/',
                'items': admin_items(User, Group),
            },
            {
                'title': 'Другое',
                'url': '/admin/main/',
                'items': admin_items(Tag, RedirectPage),
            },
        ]
    }
