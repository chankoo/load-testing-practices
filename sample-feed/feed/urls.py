from django.urls import path
from .views import PostListCreateView, HealthCheckView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('health-check/', HealthCheckView.as_view(), name='health-check'),
]
