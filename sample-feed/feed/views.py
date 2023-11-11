from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from django.conf import settings
import pickle


class PostListCreateView(generics.ListCreateAPIView):
    queryset = None
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset_bytes = settings.REDIS_CLIENT.get('posts')
        if not queryset_bytes:
            queryset = Post.objects.all()
            queryset_bytes = pickle.dumps(queryset)
            settings.REDIS_CLIENT.set('posts', queryset_bytes)
        queryset = pickle.loads(queryset_bytes)
        return queryset
