from unittest import mock

from health_check.backends import BaseHealthCheckBackend
from health_check.exceptions import HealthCheckException

from directory_healthcheck import views

from django.urls import reverse


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


class UnhealthyTestView(views.BaseHealthCheckAPIView):
    def create_service_checker(self):
        return UnhealthyServiceChecker()


class HealthyTestView(views.BaseHealthCheckAPIView):
    def create_service_checker(self):
        return HealthyServiceChecker()


def test_health_check_no_token(rf):
    request = rf.get('/')
    response = HealthyTestView.as_view()(request)

    assert response.status_code == 403


def test_health_check_valid_token(rf):
    request = rf.get('/', {'token': 'debug'})
    response = HealthyTestView.as_view()(request)

    assert response.status_code == 200
    assert response.render().content == (
        b'<?xml version="1.0" encoding="UTF-8"?>\n'
        b'<pingdom_http_custom_check>\n    '
        b'<status>OK</status>\n    '
        b'<response_time>0.0000</response_time>\n'
        b'</pingdom_http_custom_check>\n'
    )


def test_unhealthy_check_valid_token(rf):
    request = rf.get('/', {'token': 'debug'})
    response = UnhealthyTestView.as_view()(request)

    assert response.status_code == 500
    assert response.render().content == (
        b'<?xml version="1.0" encoding="UTF-8"?>\n'
        b'<pingdom_http_custom_check>\n    '
        b'<status>unknown error: error</status>\n    '
        b'<response_time>0.0000</response_time>\n'
        b'</pingdom_http_custom_check>\n'
    )


@mock.patch(
    'directory_healthcheck.backends.APIBackend.run_check',
    mock.Mock(return_value=True)
)
@mock.patch(
    'directory_healthcheck.views.BaseHealthCheckAPIView.has_permission',
    mock.Mock(return_value=True)
)
def test_api_view(client):
    response = client.get(reverse('api'))

    assert response.status_code == 200


@mock.patch(
    'directory_healthcheck.backends.SingleSignOnBackend.run_check',
    mock.Mock(return_value=True)
)
@mock.patch(
    'directory_healthcheck.views.BaseHealthCheckAPIView.has_permission',
    mock.Mock(return_value=True)
)
def test_sso_view(client):
    response = client.get(reverse('sso'))

    assert response.status_code == 200


@mock.patch(
    'directory_healthcheck.backends.SentryBackend.run_check',
    mock.Mock(return_value=True)
)
@mock.patch(
    'directory_healthcheck.views.BaseHealthCheckAPIView.has_permission',
    mock.Mock(return_value=True)
)
def test_sentry_view(client):
    response = client.get(reverse('sentry'))

    assert response.status_code == 200


@mock.patch(
    'directory_healthcheck.backends.FormsAPIBackend.run_check',
    mock.Mock(return_value=True)
)
@mock.patch(
    'directory_healthcheck.views.BaseHealthCheckAPIView.has_permission',
    mock.Mock(return_value=True)
)
def test_forms_api_view(client):
    response = client.get(reverse('forms-api'))

    assert response.status_code == 200


@mock.patch(
    'directory_healthcheck.backends.CMSAPIBackend.run_check',
    mock.Mock(return_value=True)
)
@mock.patch(
    'directory_healthcheck.views.BaseHealthCheckAPIView.has_permission',
    mock.Mock(return_value=True)
)
def test_cms_api_view(client):
    response = client.get(reverse('cms'))

    assert response.status_code == 200


def test_ping_view(client):
    response = client.get(reverse('ping'))

    assert response.status_code == 200
