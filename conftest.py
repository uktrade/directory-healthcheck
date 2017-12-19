def pytest_configure():
    from django.conf import settings
    settings.configure(
        HEALTH_CHECK_TOKEN='debug',
        INSTALLED_APPS=[
            'health_check',
            'directory_healthcheck',
        ],
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'OPTIONS': {
                    'loaders': [
                        'django.template.loaders.app_directories.Loader',
                    ],
                },
            },
        ]
    )
