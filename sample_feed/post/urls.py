from django.urls import path
from .views import PostListCreateView

urlpatterns = [
    path('me/posts/', PostListCreateView.as_view(), name='post-list-create'),
]
