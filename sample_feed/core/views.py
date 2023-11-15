from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class HealthCheckView(APIView):
    """
    Health Check API View to check the status of the application.
    """

    def get(self, request, *args, **kwargs):
        return Response({"status": "Healthy"}, status=status.HTTP_200_OK)
