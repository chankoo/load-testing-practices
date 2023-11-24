from sample_feed.core.views import BaseAPIView
from rest_framework.response import Response
from sample_feed.post.serializers import FeedPostSerializer
from .caches import FeedCacheWrapper
from .tasks import update_feed_cache
from .models import PersonRelation


class MyFeedView(BaseAPIView):
    def get(self, request, *args, **kwargs):
        # me who?
        posts = []
        return Response({"data": FeedPostSerializer(posts, many=True).data})


class FeedView(BaseAPIView):
    def get(self, request, *args, **kwargs):
        fc = FeedCacheWrapper()
        posts = fc.get_feed(owner=kwargs["person_id"])
        return Response({"data": FeedPostSerializer(posts, many=True).data})


class FeedPostsView(BaseAPIView):
    def post(self, request, *args, **kwargs):
        post = request.data.copy()

        related_persons = PersonRelation.objects.filter(
            person=post["person"],
            relation_type='friend'
        ).values_list('related_person', flat=True)
        update_feed_cache.delay(post=post, related_persons=list(related_persons))
        return super(FeedPostsView, self).post(request, *args, **kwargs)
