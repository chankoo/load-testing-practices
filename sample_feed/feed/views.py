from sample_feed.core.views import BaseAPIView
from sample_feed.feed.models import FeedRecord
from rest_framework.response import Response
from .serializers import FeedRecordSerializer


class MyFeedView(BaseAPIView):
    def get(self, request, *args, **kwargs):
        records = FeedRecord.objects.exclude(hide=True)
        return Response({"data": FeedRecordSerializer(records, many=True).data})


class FeedView(BaseAPIView):
    def get(self, request, *args, **kwargs):
        records = FeedRecord.objects.filter(person=kwargs["person_id"]).exclude(hide=True)
        return Response({"data": FeedRecordSerializer(records, many=True).data})


class FeedRecordsView(BaseAPIView):
    def post(self, request, *args, **kwargs):
        serializer = FeedRecordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return super(FeedRecordsView, self).post(request, *args, **kwargs)