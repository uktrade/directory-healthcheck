import directory_healthcheck.views
from django.urls import path

urlpatterns = [
    path(
        r"^healthcheck/$",
        directory_healthcheck.views.HealthcheckView.as_view(),
        name="healthcheck",
    ),
    path(
        r"^healthcheck/ping/$",
        directory_healthcheck.views.PingView.as_view(),
        name="healthcheck-ping",
    ),
]
