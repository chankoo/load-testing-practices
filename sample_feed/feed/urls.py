from django.urls import path
from .views import MyFeedView, FeedView, FeedRecordsView

urlpatterns = [
    path('me/feed/', MyFeedView.as_view(), name='my-feed'),
    path('<int:person_id>/feed/', FeedView.as_view(), name='feed'),
    path('feed_records/', FeedRecordsView.as_view(), name='feed-records'),
]
