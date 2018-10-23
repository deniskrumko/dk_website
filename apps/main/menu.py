from collections import namedtuple

from django.shortcuts import reverse

MenuItem = namedtuple('MenuItem', ['name', 'url', 'color', 'visible'])
HiddenMenuItem = namedtuple('HiddenMenuItem', ['name', 'url'])
MenuColor = namedtuple('MenuColor', ['accent', 'darker', 'base'])


def get_menu():
    """Method to get dictionary with menu items."""
    return {
        'index': MenuItem(
            name='Главная',
            url=reverse('main:index'),
            color=MenuColor('#4A72B7', '#4A72B7', '#666'),
            visible=True,
        ),
        'blog': MenuItem(
            name='Блог',
            url=reverse('blog:index'),
            color=MenuColor('#1BBC9C', '#1BBC9C', '#666'),
            visible=True,
        ),
        'news': MenuItem(
            name='Новости',
            url=reverse('news:index'),
            color=MenuColor('#efb900', '#ddac04', '#666'),
            visible=True,
        ),
        'music': MenuItem(
            name='Музыка',
            url=reverse('music:index'),
            color=MenuColor('#f45c28', '#f45c28', '#666'),
            visible=True,
        ),
        'diary': MenuItem(
            name='Дневник',
            url=reverse('diary:index'),
            color=MenuColor('#00B5AD', '#00B5AD', '#666'),
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
