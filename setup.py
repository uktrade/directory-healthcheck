from setuptools import find_packages, setup

setup(
    name="directory_healthcheck",
    version="3.0.2",
    url="https://github.com/uktrade/directory-healthcheck",
    license="MIT",
    author="Department for International Trade",
    description="Library to streamline healthchecks for Directory apps.",
    packages=find_packages(exclude=["tests.*", "tests"]),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    package_data={
        "directory_healthcheck": ["templates/directory_healthcheck/healthcheck.html"],
    },
    include_package_data=True,
    install_requires=[
        "django-health-check==3.16.5",
        "django>=1.11.22,<4.0.0",
    ],
    extras_require={
        "test": [
            "pytest==3.10.0",
            "pytest-cov==2.7.1",
            "pytest-django==3.5.0",
            "flake8==5.0.4",
            "codecov>=2.0.16",
            "twine>=1.11.0,<2.0.0",
            "wheel>=0.31.0,<1.0.0",
            "raven==5.19.0",
            "setuptools>=59.6.0,<66.1.0",
            "directory-sso-api-client",
            "directory-api-client",
            "directory-forms-api-client",
            "directory-cms-client",
            "directory-client-core>=4.3.0,<7.1.0",
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
