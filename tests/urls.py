from django.conf.urls import url

import directory_healthcheck.views


urlpatterns = [
    url(
        r'^api/$',
        directory_healthcheck.views.APIHealthcheckView.as_view(),
        name='api'
    ),
    url(
        r'^sso/$',
        directory_healthcheck.views.SingleSignOnHealthcheckView.as_view(),
        name='sso'
    ),
    url(
        r'^sentry/$',
        directory_healthcheck.views.SentryHealthcheckView.as_view(),
        name='sentry'
    ),
    url(
        r'^forms-api/$',
        directory_healthcheck.views.FormsAPIBackendHealthcheckView.as_view(),
        name='forms-api'
    ),
    url(
        r'^cms/$',
        directory_healthcheck.views.CMSAPIBackendHealthcheckView.as_view(),
        name='cms'
    ),
    url(
        r'^ping/$',
        directory_healthcheck.views.PingView.as_view(),
        name='ping'
    ),
]
