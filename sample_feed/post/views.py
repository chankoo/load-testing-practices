import pickle
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from sample_feed.core.caches import RedisCacheWrapper


class PostListCreateView(generics.ListCreateAPIView):
    queryset = None
    serializer_class = PostSerializer

    def get_queryset(self):
        redis_client = RedisCacheWrapper().rd
        queryset_bytes = redis_client.get('posts')
        if not queryset_bytes:
            queryset = Post.objects.all()
            queryset_bytes = pickle.dumps(queryset)
            redis_client.set('posts', queryset_bytes)
        queryset = pickle.loads(queryset_bytes)
        return queryset
