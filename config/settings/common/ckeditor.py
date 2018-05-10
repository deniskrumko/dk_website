CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'width': '100%',
        'height': 240,
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            [
                'NumberedList',
                'BulletedList',
                'HorizontalRule',
                '-',
                'Outdent',
                'Indent',
                'Iframe',
                '-',
                'JustifyLeft',
                'JustifyCenter',
                'JustifyRight',
                'JustifyBlock'
            ],
            ['Link', 'Unlink', 'Image'],
            ['TextColor', 'BGColor'],
            ['RemoveFormat', 'Source']
        ],
        'extraPlugins': ','.join([
            'iframe'
        ]),
    },
    'preview': {
        'toolbar': 'Custom',
        'width': '100%',
        'height': 120,
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            [
                'NumberedList',
                'BulletedList',
                'HorizontalRule',
                '-',
                'Outdent',
                'Indent',
                '-',
                'JustifyLeft',
                'JustifyCenter',
                'JustifyRight',
                'JustifyBlock'
            ],
            ['Link', 'Unlink', 'Image'],
            ['TextColor', 'BGColor'],
            ['RemoveFormat', 'Source']
        ]
    },
}
