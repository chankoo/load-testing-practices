from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from django.conf import settings
import pickle


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
        queryset_bytes = settings.REDIS_CLIENT.get('posts')
        if not queryset_bytes:
            queryset = Post.objects.all()
            queryset_bytes = pickle.dumps(queryset)
            settings.REDIS_CLIENT.set('posts', queryset_bytes)
        queryset = pickle.loads(queryset_bytes)
        return queryset


