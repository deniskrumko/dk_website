from django.shortcuts import reverse
from collections import namedtuple

MenuItem = namedtuple('MenuItem', ['name', 'url', 'color'])
MenuColor = namedtuple('MenuColor', ['accent', 'base'])


def get_menu():
    return {
        'index': MenuItem(
            name='Главная',
            url=reverse('main:index'),
            color=MenuColor('#5a6f83', '#333')
        ),
        'diary': MenuItem(
            name='Дневник',
            url=reverse('diary:index'),
            color=MenuColor('#fd81a8', '#f0f0f0')
        ),
        'music': MenuItem(
            name='Музыка',
            url=reverse('music:index'),
            color=MenuColor('#f35d28', '#f0f0f0')
        ),
        'admin': MenuItem(
            name='Админка',
            url=reverse('admin:index'),
            color=MenuColor('#f35d28', '#f0f0f0')
        ),
    }
