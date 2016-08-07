from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework import permissions
from simple_login.views import(
    AccountActivationAPIView,
    RequestActivationKey,
    LoginAPIView,
    RetrieveUpdateDestroyProfileView,
    RequestPasswordReset,
    ChangePassword,
)

from printing_app.models import Album, Photo, User
from printing_app.serializers import(
    AlbumSerializer,
    PhotoSerializer,
    UserSerializer,
)


class Register(CreateAPIView):
    serializer_class = UserSerializer


class ActivationKey(RequestActivationKey):
    user_model = User


class Activate(AccountActivationAPIView):
    user_model = User
    serializer_class = UserSerializer


class Login(LoginAPIView):
    user_model = User
    serializer_class = UserSerializer


class ForgotPassword(RequestPasswordReset):
    user_model = User


class ChangePasswordView(ChangePassword):
    user_model = User


class Profile(RetrieveUpdateDestroyProfileView):
    user_model = User
    serializer_class = UserSerializer


class ListCreateAlbum(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = AlbumSerializer

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        request.data.update({'owner': request.user.id})
        return super().post(request, *args, **kwargs)


class AlbumView(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = AlbumSerializer

    def get_queryset(self):
        return Album.objects.filter(
            id=self.kwargs['pk'],
            owner=self.request.user
        )


class CreatePhoto(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = PhotoSerializer

    def post(self, request, *args, **kwargs):
        request.data.update({'album': self.kwargs['pk']})
        request.data.update({'owner': request.user.id})
        return super().post(request, *args, **kwargs)


class PhotoView(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = PhotoSerializer

    def get_queryset(self):
        return Photo.objects.filter(
            id=self.kwargs['pk'],
            album_id=self.kwargs['album']
        )
