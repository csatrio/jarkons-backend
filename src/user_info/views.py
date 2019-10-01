from http import HTTPStatus

from rest_framework.decorators import api_view
from rest_framework.response import Response
from common.jsonbody import Jsonbody
from common.models import get_user_model
from common.utils import delete_keys
from django.conf import settings
from django.contrib.auth.hashers import make_password
from .models import UserInfo


@api_view(['POST'])
def register(request):
    body = Jsonbody(request.body)

    if body.email and get_user_model().objects.filter(email__iexact=body.email).count() > 0:
        return Response({'message': 'user already registered !'}, status=HTTPStatus.CONFLICT)

    user = get_user_model().objects.create(**{
        'first_name': body.nama_depan,
        'last_name': body.nama_belakang,
        'username': body.username,
        'password': make_password(body.password),
        'email': body.email
    })

    delete_keys(body.json, 'username', 'password', 'email', 'nama_depan', 'nama_belakang')
    body.json['user_id'] = user.id

    user_info = UserInfo.objects.create(**body.json)

    return Response({'id': user.id, 'user_info_id': user_info.id, 'username': body.username, 'email': body.email})
