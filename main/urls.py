from django.urls import path

from main.apps import MainConfig
from main.views import PostCreateAPIView, PostDestroyAPIView, PostUpdateAPIView, PostRetrieveAPIView, PostListAPIView, \
    CommentCreateAPIView, CommentDestroyAPIView, CommentUpdateAPIView, CommentRetrieveAPIView, CommentListAPIView

app_name = MainConfig.name


urlpatterns = [
    path("post/create/", PostCreateAPIView.as_view(), name="Post-create"),
    path("post/list/", PostListAPIView.as_view(), name="Post-list"),
    path("post/<int:pk>/detail", PostRetrieveAPIView.as_view(), name="Post-detail"),
    path("post/<int:pk>/update", PostUpdateAPIView.as_view(), name="Post-update"),
    path("post/<int:pk>/delete", PostDestroyAPIView.as_view(), name="Post-destroy"),

    path("comment/create/", CommentCreateAPIView.as_view(), name="Comment-create"),
    path("comment/list/", CommentListAPIView.as_view(), name="Comment-list"),
    path("comment/<int:pk>/detail", CommentRetrieveAPIView.as_view(), name="Comment-detail"),
    path("comment/<int:pk>/update", CommentUpdateAPIView.as_view(), name="Comment-update"),
    path("comment/<int:pk>/delete", CommentDestroyAPIView.as_view(), name="Comment-destroy"),
]
