import pytest

from django.conf import settings
from django.core.urlresolvers import reverse


def test_health_check_no_token(client):
    response = client.get(reverse('health-check'))

    assert response.status_code == 403


def test_health_check_valid_token(client):
    response = client.get(
        reverse('health-check'),
        {'token': settings.HEALTH_CHECK_TOKEN}
    )

    assert response.status_code == 200
