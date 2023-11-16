from sample_feed.core.views import BaseAPIView
from sample_feed.feed.models import FeedRecord, PersonRelation
from rest_framework.response import Response
from .serializers import FeedRecordSerializer


class MyFeedView(BaseAPIView):
    def get(self, request, *args, **kwargs):
        records = FeedRecord.objects.exclude(hide=True)
        return Response({"data": FeedRecordSerializer(records, many=True).data})


class FeedView(BaseAPIView):
    def get(self, request, *args, **kwargs):
        records = FeedRecord.objects.filter(owner=kwargs["person_id"]).exclude(hide=True)
        return Response({"data": FeedRecordSerializer(records, many=True).data})


class FeedRecordsView(BaseAPIView):
    def post(self, request, *args, **kwargs):
        data = request.data

        # Add a FeedRecord for me
        serializer = FeedRecordSerializer(data={**data, "owner": data["person"]})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Add FeedRecords for friends of mine
        relations = PersonRelation.objects.filter(person=data["person"], relation_type='friend')
        for relation in relations:
            serializer = FeedRecordSerializer(data={**data, "owner": relation.related_person})
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return super(FeedRecordsView, self).post(request, *args, **kwargs)