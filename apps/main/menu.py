from collections import namedtuple

from django.shortcuts import reverse

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
        'blog': MenuItem(
            name='Блог',
            url=reverse('blog:index'),
            color=MenuColor('#1BAEC1', '#666'),
            auth=False,
        ),
        'music': MenuItem(
            name='Музыка',
            url=reverse('music:index'),
            color=MenuColor('#f45c28', '#666'),
            auth=False,
        ),
    }
