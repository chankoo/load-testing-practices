from django.urls import include, path

urlpatterns = [
    path('v1/', include('sample_feed.core.urls')),
    path('v1/', include('sample_feed.post.urls')),
]
