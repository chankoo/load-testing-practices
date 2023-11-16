from rest_framework import serializers
from .models import FeedRecord


class FeedRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedRecord
        fields = ['id', 'person', 'post', 'hide', 'created_at', 'updated_at']
