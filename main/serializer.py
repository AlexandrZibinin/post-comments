from rest_framework import serializers

from main.models import Post, Comment
from main.validators import validate_title


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[validate_title])

    class Meta:
        model = Post
        fields = ("title", "text", "image", "author", "created_at", "updated_at")
        read_only_fields = (
            "author",
            "created_at",
            "updated_at",
        )


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post", "text", "author", "created_at", "updated_at")
        read_only_fields = (
            "post",
            "author",
            "created_at",
            "updated_at",
        )
