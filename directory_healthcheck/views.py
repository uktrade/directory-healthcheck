from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden
from django.utils.crypto import constant_time_compare
from django.views import View
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView

from directory_healthcheck import backends


class BaseHealthCheckAPIView(TemplateView):
    template_name = 'directory_healthcheck/healthcheck.html'
    service_checker = None

    def create_service_checker(self):
        raise NotImplemented()

    def has_permission(self):
        return constant_time_compare(
            self.request.GET.get('token'),
            settings.HEALTH_CHECK_TOKEN
        )

    @never_cache
    def get(self, *args, **kwargs):
        if not self.has_permission():
            return HttpResponseForbidden()
        self.service_checker = self.create_service_checker()
        self.service_checker.run_check()
        return super().get(*args, **kwargs)

    def render_to_response(self, *args, **kwargs):
        if self.service_checker.errors:
            kwargs['status'] = 500
        return super().render_to_response(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        return {
            'service_checker': self.service_checker
        }


class APIHealthcheckView(BaseHealthCheckAPIView):
    def create_service_checker(self):
        return backends.APIBackend()


class SingleSignOnHealthcheckView(BaseHealthCheckAPIView):
    def create_service_checker(self):
        return backends.SingleSignOnBackend()


class SentryHealthcheckView(BaseHealthCheckAPIView):
    def create_service_checker(self):
        return backends.SentryBackend()


class FormsAPIBackendHealthcheckView(BaseHealthCheckAPIView):
    def create_service_checker(self):
        return backends.FormsAPIBackend()


class CMSAPIBackendHealthcheckView(BaseHealthCheckAPIView):
    def create_service_checker(self):
        return backends.CMSAPIBackend()


class PingView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('OK')
