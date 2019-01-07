# directory-healthcheck

[![code-climate-image]][code-climate]
[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]
[![pypi-image]][pypi]

**Wrapper around [django-health-check](https://github.com/KristianOellegaard/django-health-check) to streamline health checks in [directory apps](https://github.com/uktrade/?utf8=%E2%9C%93&q=directory&type=&language=).**

---

## Installation

```shell
pip install directory-healthcheck
```

## Usage
Update your `settings.py`:

```py
import directory_healthcheck.backends


INSTALLED_APPS = [
    ...
    'directory_healthcheck',
    ...
]

DIRECTORY_HEALTHCHECK_TOKEN = 'some-secret-token'

DIRECTORY_HEALTHCHECK_BACKENDS [
    directory_healthcheck.backends.APIBackend,
    directory_healthcheck.backends.SingleSignOnBackend,
    directory_healthcheck.backends.FormsAPIBackend,
]

```

Update your `urls.py`:

```
    url(
        r'^healthcheck/$',
        directory_healthcheck.views.HealthcheckView.as_view(),
        name='healthcheck'
    ),

```


## Development

    $ git clone https://github.com/uktrade/directory-healthcheck
    $ cd directory-healthcheck
    $ make

## Publish to PyPI

The package should be published to PyPI on merge to master. If you need to do it locally then get the credentials from rattic and add the environment variables to your host machine:

| Setting                     |
| --------------------------- |
| DIRECTORY_PYPI_USERNAME     |
| DIRECTORY_PYPI_PASSWORD     |


Then run the following command:

    make publish


[code-climate-image]: https://codeclimate.com/github/uktrade/directory-healthcheck/badges/issue_count.svg
[code-climate]: https://codeclimate.com/github/uktrade/directory-healthcheck

[circle-ci-image]: https://circleci.com/gh/uktrade/directory-healthcheck/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/directory-healthcheck/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/directory-healthcheck/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/directory-healthcheck

[pypi-image]: https://badge.fury.io/py/directory-healthcheck.svg
[pypi]: https://badge.fury.io/py/directory-healthcheck
