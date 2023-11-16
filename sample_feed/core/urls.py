from django.urls import path
from .views import HealthCheckView, ResetDataView

urlpatterns = [
    path('health-check/', HealthCheckView.as_view(), name='health-check'),
    path('reset-data/', ResetDataView.as_view(), name='reset-data/'),
]
