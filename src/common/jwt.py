from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from user_info.models import UserInfo


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(CustomTokenObtainPairSerializer, cls).get_token(user)
        # Add custom claims
        token_attributes = {
            'user': user.username
        }
        for key, value in token_attributes.items():
            token[key] = value
        # ...
        return token


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        user = serializer.user
        user_info = UserInfo.objects.filter(user_id=user.id)

        if len(user_info) > 0:
            user_info = user_info[0]
        else:
            return Response({'message': 'Pengisian data user tidak benar, mohon perbaiki data user terkait !'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            user_photo = user_info.pas_photo.url()
        except ValueError:
            user_photo = None

        serializer.validated_data.update({
            'id': user.id,
            'user_info_id': user_info.id,
            'pas_photo': user_photo,
            'username': user.username,
            'email': user.email,
            'is_verified': user.is_verified,
            'gold_member': user_info.gold_member,
            'platinum_member': user_info.platinum_member,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'last_login': user.last_login
        })

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
