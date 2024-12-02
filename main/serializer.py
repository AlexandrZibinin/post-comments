from rest_framework import serializers

from main.models import Post, Comment
from main.validators import validate_title


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[validate_title])
    class Meta:
        model = Post
        fields = ("__all__",)
        read_only_fields = (
            "author",
            "created_at",
            "updated_at",
        )


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("__all__",)
        read_only_fields = (
            "author",
            "created_at",
            "updated_at",
        )