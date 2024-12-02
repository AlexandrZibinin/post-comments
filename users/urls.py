from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UsersCreateAPIView, UsersListAPIView, UsersDetailAPIView, UsersUpdateAPIView, \
    UsersDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("create/", UsersCreateAPIView.as_view(), name="users-create"),
    path("list/", UsersListAPIView.as_view(), name="users-list"),
    path("<int:pk>/detail", UsersDetailAPIView.as_view(), name="users-detail"),
    path("<int:pk>/update", UsersUpdateAPIView.as_view(), name="users-update"),
    path("<int:pk>/delete", UsersDestroyAPIView.as_view(), name="users-delete"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
