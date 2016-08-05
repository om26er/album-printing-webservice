from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from printing_app.models import User, Album, Photo


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(required=True, write_only=True)
    full_name = serializers.CharField(required=True)
    mobile_number = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'full_name',
            'mobile_number',
        )


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'photo')


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Album
        fields = ('id', 'name', 'photos')
