from health_check.backends import BaseHealthCheckBackend
from health_check.exceptions import HealthCheckException
from health_check.plugins import plugin_dir
import pytest

from django.urls import reverse


@pytest.fixture(autouse=True)
def backends():
    unaltered_value = plugin_dir._registry
    yield plugin_dir
    plugin_dir._registry = unaltered_value


class UnhealthyServiceChecker(BaseHealthCheckBackend):
    def check_status(self):
        raise HealthCheckException('error')

    def run_check(self):
        super().run_check()
        self.time_taken = 0


class HealthyServiceChecker(BaseHealthCheckBackend):
    def check_status(self):
        return True

    def run_check(self):
        super().run_check()
        self.time_taken = 0


def test_health_check_no_token(client):
    response = client.get(reverse('healthcheck'))

    assert response.status_code == 403


def test_health_check_valid_token(client, settings, backends):
    backends.register(HealthyServiceChecker)
    url = reverse('healthcheck')
    response = client.get(url, {'token': settings.DIRECTORY_HEALTHCHECK_TOKEN})

    assert response.status_code == 200
    assert response.render().content == (
        b'<?xml version="1.0" encoding="UTF-8"?>'
        b'<pingdom_http_custom_check><status>\n    \n        '
        b'OK\n    \n    '
        b'</status>'
        b'<response_time>0</response_time>'
        b'</pingdom_http_custom_check>\n'
    )


def test_unhealthy_check_valid_token(client, settings, backends):
    backends.register(UnhealthyServiceChecker)
    url = reverse('healthcheck')
    response = client.get(url, {'token': settings.DIRECTORY_HEALTHCHECK_TOKEN})

    assert response.status_code == 500
    assert response.render().content == (
        b'<?xml version="1.0" encoding="UTF-8"?>'
        b'<pingdom_http_custom_check>'
        b'<status>\n    \n        '
        b'UnhealthyServiceChecker: unknown error: error\n    \n    '
        b'</status><response_time>0</response_time>'
        b'</pingdom_http_custom_check>\n'
    )


def test_ping(client):
    url = reverse('healthcheck-ping')
    response = client.get(url)

    assert response.status_code == 200
