from django.conf.urls import url

import directory_healthcheck.views


urlpatterns = [
    url(
        r'^healthcheck/$',
        directory_healthcheck.views.HealthcheckView.as_view(),
        name='healthcheck'
    ),
    url(
        r'^healthcheck/ping/$',
        directory_healthcheck.views.PingView.as_view(),
        name='healthcheck-ping'
    ),
]
