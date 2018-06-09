from django.shortcuts import reverse
from collections import namedtuple

MenuItem = namedtuple('MenuItem', ['name', 'url', 'color'])
MenuColor = namedtuple('MenuColor', ['accent', 'base'])


def get_menu():
    return {
        'index': MenuItem(
            name='Главная',
            url=reverse('main:index'),
            color=MenuColor('#5a6f83', '#ABB2C0')
        ),
        'diary': MenuItem(
            name='Дневник',
            url=reverse('diary:index'),
            color=MenuColor('#00B5AD', '#ABB2C0')
        ),
        'music': MenuItem(
            name='Музыка',
            url=reverse('music:index'),
            color=MenuColor('#f35d28', '#ABB2C0')
        ),
        'admin': MenuItem(
            name='Админка',
            url=reverse('admin:index'),
            color=MenuColor('#f35d28', '#ABB2C0')
        ),
    }
