# directory-healthcheck

[![code-climate-image]][code-climate]
[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]
[![gemnasium-image]][gemnasium]

**Wrapper around [django-health-check](https://github.com/KristianOellegaard/django-health-check) to streamline health checks in [directory apps](https://github.com/uktrade/?utf8=%E2%9C%93&q=directory&type=&language=).**

---

## Usage
In `settings.py` add the following to settings `INSTALLED_APPS`:

`directory_healthcheck`

In `settings.py` state which health check backends should be used, e.g.:

```
DIRECTORY_HEALTHCHECK_BACKENDS = [
    directory_healthcheck.backends.db
    directory_healthcheck.backends.cache,
    directory_healthcheck.backends.elastic_search,
    directory_healthcheck.backends.sentry,
]
```

## Installation

```shell
pip install -e git+https://git@github.com/uktrade/directory-healthcheck.git@v0.1.0#egg=directory-healthcheck
```

## Development

    $ git clone https://github.com/uktrade/directory-healthcheck
    $ cd directory-healthcheck
    $ make


[code-climate-image]: https://codeclimate.com/github/uktrade/directory-healthcheck/badges/issue_count.svg
[code-climate]: https://codeclimate.com/github/uktrade/directory-healthcheck

[circle-ci-image]: https://circleci.com/gh/uktrade/directory-healthcheck/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/directory-healthcheck/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/directory-healthcheck/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/directory-healthcheck

[gemnasium-image]: https://gemnasium.com/badges/github.com/uktrade/directory-healthcheck.svg
[gemnasium]: https://gemnasium.com/github.com/uktrade/directory-healthcheck
