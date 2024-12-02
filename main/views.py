from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from main.models import Post, Comment
from main.serializer import PostSerializer, CommentsSerializer
from users.permissions import IsOwnerPermissions


class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        post = serializer.save()
        post.author = self.request.user
        post.save()


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (AllowAny,)


class PostRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (AllowAny,)


class PostUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAdminUser | IsOwnerPermissions,)


class PostDestroyAPIView(generics.DestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAdminUser | IsOwnerPermissions,)


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        comment = serializer.save()
        comment.author = self.request.user
        comment.save()


class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentsSerializer
    queryset = Comment.objects.all()
    permission_classes = (AllowAny,)


class CommentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CommentsSerializer
    queryset = Comment.objects.all()
    permission_classes = (AllowAny,)


class CommentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CommentsSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsAdminUser | IsOwnerPermissions,)


class CommentDestroyAPIView(generics.DestroyAPIView):
    serializer_class = CommentsSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsAdminUser | IsOwnerPermissions,)
