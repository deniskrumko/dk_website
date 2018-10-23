from collections import namedtuple

from django.shortcuts import reverse

MenuItem = namedtuple('MenuItem', ['name', 'url', 'color', 'visible'])
HiddenMenuItem = namedtuple('HiddenMenuItem', ['name', 'url'])
MenuColor = namedtuple('MenuColor', ['accent', 'base'])


def get_menu():
    """Method to get dictionary with menu items."""
    return {
        'index': MenuItem(
            name='Главная',
            url=reverse('main:index'),
            color=MenuColor('#5a80a4', '#666'),
            visible=True,
        ),
        'blog': MenuItem(
            name='Блог',
            url=reverse('blog:index'),
            color=MenuColor('#1BBC9C', '#666'),
            visible=True,
        ),
        'music': MenuItem(
            name='Музыка',
            url=reverse('music:index'),
            color=MenuColor('#f45c28', '#666'),
            visible=True,
        ),
        'diary': MenuItem(
            name='Дневник',
            url=reverse('diary:index'),
            color=MenuColor('#00B5AD', '#666'),
            visible=False,
        ),
    }


def get_hidden_menu():
    """Method to get tuple of hidden menu items (for superuser only)."""
    return (
        HiddenMenuItem(
            name='Дневник',
            url=reverse('diary:index'),
        ),
        HiddenMenuItem(
            name='Админка',
            url=reverse('admin:index'),
        ),
        HiddenMenuItem(
            name='Выйти',
            url=reverse('users:logout'),
        ),
    )
