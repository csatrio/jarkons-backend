from http import HTTPStatus

from rest_framework.decorators import api_view
from rest_framework.response import Response
from common.jsonbody import Jsonbody
from common.models import get_user_model
from common.utils import delete_keys, build_query_param
from django.contrib.auth.hashers import make_password
from rest_framework import generics, serializers

from .models import UserInfo, Product


@api_view(['POST'])
def register(request):
    body = Jsonbody(request.body)

    if body.email and get_user_model().objects.filter(email__iexact=body.email).count() > 0:
        return Response({'message': 'user already registered !'}, status=HTTPStatus.CONFLICT)

    names = body.nama.split(' ')
    user = get_user_model().objects.create(**{
        'first_name': names[0],
        'last_name': names[1] if len(names) > 1 else names[0],
        'username': body.email,
        'password': make_password(body.password),
        'email': body.email
    })

    delete_keys(body.json, 'password', 'email', 'nama')
    body.json['user_id'] = user.id

    user_info = UserInfo.objects.create(**body.json)

    return Response({'id': user.id, 'user_info_id': user_info.id, 'nama': body.nama, 'email': body.email})


class PerusahaanSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UserInfo


class search_perusahaan(generics.ListAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = PerusahaanSerializer

    def get_queryset(self):
        query_param = build_query_param(self.request, **{
            'nama': 'nama__icontains',
            'nama_perusahaan': 'nama_perusahaan__icontains',
            'id': 'id__iexact',
            'klasifikasi__id': 'klasifikasi__id__iexact',
            'kualifikasi_profesi': 'kualifikasi__profesi__text__icontains',
            'kualifikasi': 'kualifikasi__text__icontains',
            'provinsi': 'provinsi__text__icontains',
            'kabupaten_kota': 'kabupaten_kota__text__icontains',
        })
        return UserInfo.objects.filter(**query_param)

    def get_serializer_class(self):
        return super(generics.ListAPIView, self).get_serializer_class()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Product


class search_produk(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        query_param = build_query_param(self.request, **{
            'nama_produk': 'nama_produk__icontains',
            'nama_perusahaan': 'nama_perusahaan__icontains',
            'id': 'id__iexact',
            'klasifikasi__id': 'klasifikasi__id__iexact',
            'kualifikasi_profesi': 'kualifikasi__profesi__text__icontains',
            'kualifikasi': 'kualifikasi__text__icontains',
            'provinsi': 'provinsi__text__icontains',
            'kabupaten_kota': 'kabupaten_kota__text__icontains',
            'deskripsi': 'deskripsi__icontains'
        })
        return Product.objects.filter(**query_param)

    def get_serializer_class(self):
        return super(generics.ListAPIView, self).get_serializer_class()
