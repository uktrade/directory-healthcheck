from django.conf.urls import url

from directory_healthcheck import views


urlpatterns = [
    url(
        r"^$",
        views.HealthCheckAPIView.as_view(),
        name='health-check',
    ),
]
