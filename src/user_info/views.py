from http import HTTPStatus

from django.contrib.auth.hashers import make_password
from rest_framework import generics, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.components import get_generic_serializer
from common.filters import filter_q
from common.jsonbody import Jsonbody
from common.models import get_user_model
from common.utils import delete_keys, build_query_param, base64_to_file, millis, save_image_field
from .models import UserInfo, Product, Provinsi, Profesi, KabupatenKota, InfoLoker, CarouselImage


@api_view(['POST'])
def register(request):
    body = Jsonbody(request.body)

    if body.email and get_user_model().objects.filter(email__iexact=body.email).count() > 0:
        return Response({'message': 'user already registered !'}, status=HTTPStatus.CONFLICT)

    try:
        names = body.nama.split(' ')
    except Exception:
        return Response({'message': 'Nama harus diisi !'}, status=HTTPStatus.BAD_REQUEST)

    user = get_user_model().objects.create(**{
        'first_name': names[0],
        'last_name': names[1] if len(names) > 1 else names[0],
        'username': body.email,
        'password': make_password(body.password),
        'email': body.email
    })

    pas_photo = body.pas_photo
    logo_perusahaan = body.logo_perusahaan
    selfie_dengan_identitas_diri = body.selfie_dengan_identitas_diri
    delete_keys(body.json, 'password', 'email', 'nama', 'pas_photo', 'logo_perusahaan', 'selfie_dengan_identitas_diri')
    body.json['user_id'] = user.id

    user_info = UserInfo(**body.json)
    save_image_field(user_info.pas_photo, pas_photo)
    save_image_field(user_info.logo_perusahaan, logo_perusahaan)
    save_image_field(user_info.selfie_dengan_identitas_diri, selfie_dengan_identitas_diri)
    user_info.save()

    return Response({'id': user.id, 'user_info_id': user_info.id, 'nama': body.nama, 'email': body.email})


@api_view(['GET'])
def registration_info(request):
    profesi = Profesi.objects.all().values('id', 'text')
    kabupaten = {}

    for _kabupaten in KabupatenKota.objects.values('id', 'text', 'provinsi_id'):
        provinsi_id = _kabupaten['provinsi_id']
        provinsi_list = kabupaten.get(provinsi_id)
        if provinsi_list is None:
            provinsi_list = []
        provinsi_list.append({
            'id': _kabupaten['id'],
            'text': _kabupaten['text']
        })
        kabupaten[provinsi_id] = provinsi_list

    provinsi = [{
        'id': _provinsi['id'],
        'text': _provinsi['text'],
        'kabupaten_list': kabupaten[_provinsi['id']],
    } for _provinsi in Provinsi.objects.values('id', 'text')]

    return Response({
        'profesi': profesi,
        'provinsi': provinsi
    })


@api_view(['GET'])
def get_filters(request):
    profesi = Profesi.objects.all().values('id', 'text')
    provinsi = Provinsi.objects.all().values('id', 'text')

    return Response({
        'kategori': profesi,
        'lokasi': provinsi
    })


class SearchPerusahaan(generics.ListAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = get_generic_serializer(UserInfo)

    def get_queryset(self):
        q = self.request.query_params.get('q')
        query_param = build_query_param(self.request, **{
            'nama': 'nama__icontains',
            'id': 'id__iexact',

            'klasifikasiId': 'klasifikasi__id__iexact',
            'kualifikasiId': 'kualifikasi__id__iexact',
            'profesiId': 'profesi__id__iexact',
            'provinsiId': 'provinsi__id__iexact',
            'kabupatenKotaId': 'kabupaten_kota__id__iexact',

            'klasifikasi': 'klasifikasi__text__icontains',
            'kualifikasi': 'kualifikasi__text__icontains',
            'profesi': 'profesi__text__icontains',
            'provinsi': 'provinsi__text__icontains',
            'kabupaten_kota': 'kabupaten_kota__text__icontains',
        })
        queryset = UserInfo.objects.filter(**query_param)
        if q is not None:
            queryset = filter_q(queryset, ['nama', 'nama_perusahaan', 'alamat_perusahaan'], q)
        return queryset

    def get_serializer_class(self):
        return super(generics.ListAPIView, self).get_serializer_class()


class PerusahaanSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nama_perusahaan = serializers.CharField()
    logo_perusahaan = serializers.ImageField()


class ProductSerializer(serializers.ModelSerializer):
    perusahaan = PerusahaanSerializer()

    class Meta:
        model = Product
        fields = ('id', 'nama_produk', 'gambar', 'deskripsi', 'perusahaan')


class SearchProduk(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        q = self.request.query_params.get('q')
        query_param = build_query_param(self.request, **{
            'nama_produk': 'nama_produk__icontains',
            'nama_perusahaan': 'perusahaan__nama_perusahaan__icontains',
            'id': 'id__iexact',

            'klasifikasiId': 'perusahaan__klasifikasi__id__iexact',
            'kualifikasiId': 'perusahaan__kualifikasi__id__iexact',
            'profesiId': 'perusahaan__profesi__id__iexact',
            'provinsiId': 'perusahaan__provinsi__id__iexact',
            'kabupatenKotaId': 'perusahaan__kabupaten_kota__id__iexact',

            'klasifikasi': 'perusahaan__klasifikasi__text__icontains',
            'kualifikasi': 'perusahaan__kualifikasi__text__icontains',
            'profesi': 'perusahaan__profesi__text__icontains',
            'provinsi': 'perusahaan__provinsi__text__icontains',
            'kabupaten_kota': 'perusahaan__kabupaten_kota__text__icontains',

            'deskripsi': 'deskripsi__icontains'
        })
        queryset = Product.objects.select_related('perusahaan').filter(**query_param)
        if q is not None:
            queryset = filter_q(queryset, ['nama_produk', 'perusahaan__nama_perusahaan', 'deskripsi'], q)
        return queryset

    def get_serializer_class(self):
        return super(generics.ListAPIView, self).get_serializer_class()


class InfoLokerSerializerGet(serializers.ModelSerializer):
    perusahaan = PerusahaanSerializer()
    id = serializers.IntegerField()

    class Meta:
        model = InfoLoker
        fields = ('id', 'nama_pekerjaan', 'desc_pekerjaan', 'gaji', 'lokasi', 'perusahaan', 'end_date', 'created',
                  'modified', 'keahlian', 'fasilitas', 'kualifikasi')


class InfoLokerSerializerPost(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    nama_pekerjaan = serializers.CharField()
    desc_pekerjaan = serializers.CharField()
    lokasi = serializers.CharField()
    gaji = serializers.CharField()
    end_date = serializers.DateTimeField()
    perusahaan_id = serializers.IntegerField()

    class Meta:
        model = InfoLoker
        fields = ('id', 'nama_pekerjaan', 'gaji', 'desc_pekerjaan', 'lokasi', 'perusahaan_id', 'end_date', 'created',
                  'modified', 'keahlian', 'fasilitas', 'kualifikasi')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return InfoLoker.objects.create(**validated_data)


class CrudInfoVacancy(generics.ListAPIView):

    def get_queryset(self):
        q = self.request.query_params.get('q')
        query_param = build_query_param(self.request, **{
            'nama_pekerjaan': 'nama_pekerjaan__icontains',
            'desc_pekerjaan': 'desc_pekerjaan__icontains',
            'nama_perusahaan': 'perusahaan__nama_perusahaan__icontains',
            'id': 'id__iexact',
        })
        queryset = InfoLoker.objects.select_related('perusahaan').filter(**query_param)
        if q is not None:
            queryset = filter_q(queryset, ['nama_perkerjaan', 'perusahaan__nama_perusahaan', 'desc_pekerjaan'], q)
        return queryset

    def get_serializer_class(self):
        method = self.request.method
        if method == 'GET':
            return InfoLokerSerializerGet
        return InfoLokerSerializerPost
