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
In `settings.py` add the following to settings `INSTALLED_APPS`:

```
    'directory_healthcheck',
    'health_check',
```

Then add some views into your `urls.py`:

```
    url(
        r'^healthcheck/api/$',
        directory_healthcheck.views.APIHealthcheckView.as_view(),
        name='healthcheck-api'
    ),
    url(
        r'^healthcheck/sso/$',
        directory_healthcheck.views.SingleSignOnHealthcheckView.as_view(),
        name='healthcheck-sso'
    ),
```

or create your own custom views:

```
from directry_healthcheck.views import BaseHealthCheckAPIView
from health_check.backends import BaseHealthCheckBackend

class MyCustomBackend(BaseHealthCheckBackend):
    def check_status(self):
        # see directory_healthchecks.backends for examples
        ...


class APIHealthcheckView(BaseHealthCheckAPIView):
    def create_service_checker(self):
        return MyCustomBackend()

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
