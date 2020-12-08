# myapp1/urls.py

from .views import list
from django.urls import path


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("api/$", list),
    path("api/health", list),
    ]
