import pickle
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from sample_feed.services.caches import RedisCacheWrapper


class HealthCheckView(APIView):
    """
    Health Check API View to check the status of the application.
    """

    def get(self, request, *args, **kwargs):
        return Response({"status": "Healthy"}, status=status.HTTP_200_OK)


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


