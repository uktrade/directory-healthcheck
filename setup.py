from setuptools import setup, find_packages


setup(
    name='directory_healthcheck',
    version='0.5.0',
    url='https://github.com/uktrade/directory-healthcheck',
    license='MIT',
    author='Department for International Trade',
    description='Library to streamline healthchecks for Directory apps.',
    packages=find_packages(exclude=["tests.*", "tests"]),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=[
        'django-health-check==3.0.0',
        'django>=1.9,<2.0a1',
        'pytz>=2017.2',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
