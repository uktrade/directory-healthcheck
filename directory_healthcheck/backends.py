from health_check.backends import BaseHealthCheckBackend
from health_check.exceptions import (
    ServiceReturnedUnexpectedResult, ServiceUnavailable
)
from raven import Client
from raven.transport.http import HTTPTransport

from django.conf import settings


class APIBackend(BaseHealthCheckBackend):

    message_bad_status = 'API returned {0.status_code} status code'

    def check_status(self):
        from directory_api_client.client import api_client
        try:
            response = api_client.ping()
        except Exception as error:
            raise ServiceUnavailable('(API) ' + str(error))
        else:
            if response.status_code != 200:
                raise ServiceReturnedUnexpectedResult(
                    self.message_bad_status.format(response)
                )
        return True


class SigngleSignOnBackend(BaseHealthCheckBackend):

    message_bad_status = 'SSO proxy returned {0.status_code} status code'

    def check_status(self):
        from directory_sso_api_client.client import sso_api_client
        try:
            response = sso_api_client.ping()
        except Exception as error:
            raise ServiceUnavailable('(SSO proxy) ' + str(error))
        else:
            if response.status_code != 200:
                raise ServiceReturnedUnexpectedResult(
                    self.message_bad_status.format(response)
                )
        return True


class FormsAPIBackend(BaseHealthCheckBackend):

    message_bad_status = 'Forms API returned {0.status_code} status code'

    def check_status(self):
        from directory_forms_api_client.client import forms_api_client
        try:
            response = forms_api_client.ping()
        except Exception as error:
            raise ServiceUnavailable('(Forms API) ' + str(error))
        else:
            if response.status_code != 200:
                raise ServiceReturnedUnexpectedResult(
                    self.message_bad_status.format(response)
                )
        return True


class SentryBackend(BaseHealthCheckBackend):

    def check_status(self):
        client = Client(
            **settings.RAVEN_CONFIG,
            raise_send_errors=True,
            install_sys_hook=False,
            install_logging_hook=False,
            transport=HTTPTransport
        )
        try:
            client.captureMessage('healthcheck')
        except Exception as error:
            raise ServiceUnavailable('(Sentry) ' + str(error))
        return True
