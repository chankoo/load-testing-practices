from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from sample_feed.core.caches import RedisCacheWrapper
from sample_feed.scripts import clean_tables


class BaseAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_200_OK)


class HealthCheckView(BaseAPIView):
    """
    Health Check API View to check the status of the application.
    """

    def get(self, request, *args, **kwargs):
        return Response({"status": "Healthy"}, status=status.HTTP_200_OK)


class ResetDataView(BaseAPIView):
    def get(self, request, *args, **kwargs):
        success = False
        if request.GET.get('key') == settings.SECRET_KEY:
            clean_tables()
            redis = RedisCacheWrapper()
            redis.reset_redis()
            success = True
        return Response({"success": success}, status=status.HTTP_200_OK)
