from django.shortcuts import reverse
from collections import namedtuple

MenuItem = namedtuple('MenuItem', ['name', 'url', 'color', 'auth'])
MenuColor = namedtuple('MenuColor', ['accent', 'base'])


def get_menu():
    return {
        'index': MenuItem(
            name='Главная',
            url=reverse('main:index'),
            color=MenuColor('#5a80a4', '#666'),
            auth=False,
        ),
        'diary': MenuItem(
            name='Дневник',
            url=reverse('diary:index'),
            color=MenuColor('#00B5AD', '#666'),
            auth=True,
        ),
        'music': MenuItem(
            name='Музыка',
            url=reverse('music:index'),
            color=MenuColor('#f35d28', '#666'),
            auth=False,
        ),
        'admin': MenuItem(
            name='Админка',
            url=reverse('admin:index'),
            color=MenuColor('#f35d28', '#666'),
            auth=True,
        ),
    }
