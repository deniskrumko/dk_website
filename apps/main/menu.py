from collections import namedtuple

from django.shortcuts import reverse

MenuItem = namedtuple('MenuItem', ['name', 'url', 'color'])
MenuColor = namedtuple('MenuColor', ['accent', 'base'])


def get_menu():
    return {
        'index': MenuItem(
            name='Главная',
            url=reverse('main:index'),
            color=MenuColor('#5a80a4', '#666'),
        ),
        'blog': MenuItem(
            name='Блог',
            url=reverse('blog:index'),
            color=MenuColor('#1BAEC1', '#666'),
        ),
        'music': MenuItem(
            name='Музыка',
            url=reverse('music:index'),
            color=MenuColor('#f45c28', '#666'),
        ),
    }
