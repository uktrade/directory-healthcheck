from setuptools import setup, find_packages


setup(
    name='directory_healthcheck',
    version='2.0.0',
    url='https://github.com/uktrade/directory-healthcheck',
    license='MIT',
    author='Department for International Trade',
    description='Library to streamline healthchecks for Directory apps.',
    packages=find_packages(exclude=["tests.*", "tests"]),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    package_data={
        'directory_healthcheck': [
            'templates/directory_healthcheck/healthcheck.html'
        ],
    },
    include_package_data=True,
    install_requires=[
        'django-health-check==3.8.0',
        'django>=1.11.22,<3.0a1',
    ],
    extras_require={
        'test': [
            'pytest==3.10.0',
            'pytest-cov==2.7.1',
            'pytest-django==3.5.0',
            'flake8==3.7.8',
            'codecov==2.0.9',
            'twine>=1.11.0,<2.0.0',
            'wheel>=0.31.0,<1.0.0',
            'raven==5.19.0',
            'setuptools>=38.6.0,<39.0.0',
            'directory-sso-api-client',
            'directory-api-client',
            'directory-forms-api-client',
            'directory-cms-client',
            'directory-client-core>=4.3.0,<5.0.0',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
