from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from users.models import User
from users.permissions import IsOwnerPermissions
from users.serializer import UserSerializer


class UsersCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class UsersListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated | IsAdminUser, )


class UsersDetailAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated | IsAdminUser, )


class UsersUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser | IsOwnerPermissions, )


class UsersDestroyAPIView(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser, )
