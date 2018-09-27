def pytest_configure():
    from django.conf import settings
    settings.configure(
        ROOT_URLCONF='tests.urls',
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
        ],
        DEBUG=True,
        DIRECTORY_API_CLIENT_BASE_URL='debug',
        DIRECTORY_API_CLIENT_API_KEY='debug',
        DIRECTORY_API_CLIENT_SENDER_ID='debug',
        DIRECTORY_API_CLIENT_DEFAULT_TIMEOUT=1,
        DIRECTORY_SSO_API_CLIENT_BASE_URL='debug',
        DIRECTORY_SSO_API_CLIENT_API_KEY='debug',
        DIRECTORY_SSO_API_CLIENT_SENDER_ID='debug',
        DIRECTORY_SSO_API_CLIENT_DEFAULT_TIMEOUT=1,
        DIRECTORY_FORMS_API_BASE_URL='debug',
        DIRECTORY_FORMS_API_API_KEY='debug',
        DIRECTORY_FORMS_API_SENDER_ID='debug',
        DIRECTORY_FORMS_API_DEFAULT_TIMEOUT=1,
        RAVEN_CONFIG={'dsn': 'https://debug:debug@example.com/0'},
    )
