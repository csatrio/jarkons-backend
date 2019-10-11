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
        serializer.validated_data.update({
            'id': user.id,
            'user_info_id': user_info[0].id if len(user_info) > 0 else -1,
            'username': user.username,
            'email': user.email,
            'is_verified': user.is_verified,
            'gold_member': user.gold_member,
            'platinum_member': user.platinum_member,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'last_login': user.last_login
        })

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

