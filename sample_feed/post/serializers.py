import requests
import json
from rest_framework import serializers
from .models import Post
from .consts import FEED_RECORDS_URL


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
        data = PostSerializer(instance).data
        try:
            data = {
                "person": data["person"],
                "post": data["id"],
                "content": data["content"],
            }
            requests.post(FEED_RECORDS_URL, headers=headers, data=json.dumps(data))
        except Exception as e:
            raise e
        return instance
