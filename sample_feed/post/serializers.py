import requests
import json
import time
from rest_framework import serializers
from .models import Post
from .consts import FEED_POSTS_URL


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'person', 'content', 'created_at', 'updated_at']

    def create(self, validated_data):
        instance = super(PostSerializer, self).create(validated_data)
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        data = {
            "id": instance.id,
            "person": instance.person,
            "content": instance.content,
            "created_at": instance.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "updated_at": instance.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            "created_at_ts": time.mktime(instance.created_at.timetuple()),
        }
        try:
            requests.post(FEED_POSTS_URL, headers=headers, data=json.dumps(data))
        except Exception as e:
            raise e
        return instance


class FeedPostSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    person = serializers.CharField()
    content = serializers.CharField()
    created_at = serializers.CharField()
    updated_at = serializers.CharField()
