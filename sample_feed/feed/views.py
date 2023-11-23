from sample_feed.core.views import BaseAPIView
from sample_feed.feed.models import PersonRelation
from rest_framework.response import Response
from sample_feed.post.serializers import FeedPostSerializer
from .caches import FeedCacheWrapper


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
        fc = FeedCacheWrapper()

        # Add feed cache for post owner
        fc.add_feed_posts(owner=post["person"], posts=[post])

        # Add feed cache for friends of post owner
        relations = PersonRelation.objects.filter(person=post["person"], relation_type='friend')
        for relation in relations:
            owner = relation.related_person
            fc.add_feed_posts(owner=owner, posts=[post])
        return super(FeedPostsView, self).post(request, *args, **kwargs)
