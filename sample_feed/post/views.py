import pickle
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer
from sample_feed.core.caches import RedisCacheWrapper


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    invalid_cache = False

    def get(self, request, *args, **kwargs):
        self.invalid_cache = 'invalid_cache' in request.GET
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        if self.invalid_cache:
            return super().get_queryset()
        redis_client = RedisCacheWrapper().rd
        queryset_bytes = redis_client.get('posts')
        if not queryset_bytes:
            queryset = self.queryset
            queryset_bytes = pickle.dumps(queryset.all())
            redis_client.set('posts', queryset_bytes)
        queryset = pickle.loads(queryset_bytes)
        return queryset
