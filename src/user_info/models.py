from django.conf import settings
from django.db import models

from common.fields import BinaryTextField
from common.models import BaseModel


class Profesi(BaseModel):
    class Meta:
        db_table = 'profesi'
        verbose_name = 'Profesi'
        verbose_name_plural = 'Profesi'

    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Provinsi(BaseModel):
    class Meta:
        db_table = 'provinsi'
        verbose_name = 'Provinsi'
        verbose_name_plural = 'Provinsi'

    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class KabupatenKota(BaseModel):
    class Meta:
        db_table = 'kabupaten_kota'
        verbose_name = 'Kabupaten Kota'
        verbose_name_plural = 'Kabupaten Kota'

    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Klasifikasi(BaseModel):
    class Meta:
        db_table = 'klasifikasi'
        verbose_name = 'Klasifikasi'
        verbose_name_plural = 'Klasifikasi'

    text = models.CharField(max_length=255)
    profesi = models.ForeignKey(Profesi, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.text


class Kualifikasi(BaseModel):
    class Meta:
        db_table = 'kualifikasi'
        verbose_name = 'Kualifikasi'
        verbose_name_plural = 'Kualifikasi'

    text = models.CharField(max_length=255)
    profesi = models.ForeignKey(Profesi, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.text


class PengalamanKerja(BaseModel):
    class Meta:
        db_table = 'pengalaman_kerja'
        verbose_name = 'Pengalaman Kerja'
        verbose_name_plural = 'Pengalaman Kerja'

    optimize_select_related = False
    user_info = models.ForeignKey('UserInfo', related_name='pengalaman_kerja', on_delete=models.DO_NOTHING)
    uraian_pekerjaan = BinaryTextField(null=True, blank=True)
    pemberi_kerja = models.CharField(max_length=255)
    tahun_pelaksanaan = models.DateField()
    nilai_kontrak = models.DecimalField(max_digits=40, decimal_places=4)


class AlatBerat(BaseModel):
    class Meta:
        db_table = 'alat_berat'
        verbose_name = 'Alat Berat'
        verbose_name_plural = 'Alat Berat'

    optimize_select_related = False
    user_info = models.ForeignKey('UserInfo', related_name='alat_berat', on_delete=models.DO_NOTHING)
    nama_alat = models.CharField(max_length=255, null=True, blank=True)
    satuan = models.CharField(max_length=255, null=True, blank=True)
    merek = models.CharField(max_length=255, null=True, blank=True)
    tahun_pembuatan = models.IntegerField(default=0)
    keterangan = models.CharField(max_length=255, null=True, blank=True)


class Material(BaseModel):
    class Meta:
        db_table = 'material'
        verbose_name = 'Material'
        verbose_name_plural = 'Material'

    optimize_select_related = False
    user_info = models.ForeignKey('UserInfo', related_name='material', on_delete=models.DO_NOTHING)
    nama_material = models.CharField(max_length=255, null=True, blank=True)
    satuan = models.CharField(max_length=255, null=True, blank=True)
    merek = models.CharField(max_length=255, null=True, blank=True)
    harga_per_satuan = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    keterangan = models.CharField(max_length=255, null=True, blank=True)


class UserInfo(BaseModel):
    class Meta:
        db_table = 'user_info'
        verbose_name = 'User Info'
        verbose_name_plural = 'Users Info'

    optimize_select_related = False
    bersedia_mengirim_ke_lokasi_pekerjaan = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='info', on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    no_telepon = models.IntegerField(default=0)
    profesi = models.ForeignKey(Profesi, on_delete=models.DO_NOTHING)
    nama_perusahaan = models.CharField(max_length=255)
    jabatan_di_perusahaan = models.CharField(max_length=255)
    alamat_perusahaan = models.CharField(max_length=255)

    provinsi = models.ForeignKey(Provinsi, on_delete=models.DO_NOTHING)
    kabupaten_kota = models.ForeignKey(KabupatenKota, on_delete=models.DO_NOTHING)
    klasifikasi = models.ForeignKey(Klasifikasi, on_delete=models.DO_NOTHING, null=True, blank=True)
    kualifikasi = models.ForeignKey(Kualifikasi, on_delete=models.DO_NOTHING, null=True, blank=True)
    sertifikat_badan_usaha = models.ImageField(upload_to=f"docs/sertifikat_badan_usaha/%Y/%m/%D/", default=None,
                                               null=True, blank=True)
    siup_keahlian_khusus = models.ImageField(upload_to=f"docs/siup_keahlian_khusus/%Y/%m/%D/", default=None,
                                             null=True, blank=True)
    pas_photo = models.ImageField(upload_to=f"docs/pas_photo/%Y/%m/%D/", default=None,
                                  null=True, blank=True)
    selfie_dengan_identitas_diri = models.ImageField(upload_to=f"docs/selfie_dengan_identitas_diri/%Y/%m/%D/",
                                                     default=None,
                                                     null=True, blank=True)

    masalah_yang_sering_dihadapi = BinaryTextField(null=True, blank=True)
    bantuan_yang_dibutuhkan = BinaryTextField(null=True, blank=True)
    lat = models.DecimalField(max_digits=50, decimal_places=20, default=0, blank=True)
    long = models.DecimalField(max_digits=50, decimal_places=20, default=0, blank=True)

    # riwayat pendidikan
    sekolah_dasar = models.CharField(max_length=255, null=True, blank=True)
    sekolah_menengah_pertama = models.CharField(max_length=255, null=True, blank=True)
    sekolah_menengah_kejuruan = models.CharField(max_length=255, null=True, blank=True)
    universitas = models.CharField(max_length=255, null=True, blank=True)

    # sertifikat ketrampilan
    sertifikat_ketrampilan1 = models.FileField(upload_to='docs/sertifikat_ketrampilan/%Y/%m/%D/', default=None,
                                               null=True, blank=True)
    sertifikat_ketrampilan2 = models.FileField(upload_to='docs/sertifikat_ketrampilan/%Y/%m/%D/', default=None,
                                               null=True, blank=True)
    sertifikat_ketrampilan3 = models.FileField(upload_to='docs/sertifikat_ketrampilan/%Y/%m/%D/', default=None,
                                               null=True, blank=True)

    # pengalaman kerja
    pengalaman_kerja1 = models.CharField(max_length=255, null=True, blank=True)
    pengalaman_kerja2 = models.CharField(max_length=255, null=True, blank=True)
    surat_keterangan_kerja1 = models.FileField(upload_to='docs/surat_keterangan_kerja/%Y/%m/%D/', default=None,
                                               null=True, blank=True)
    surat_keterangan_kerja2 = models.FileField(upload_to='docs/surat_keterangan_kerja/%Y/%m/%D/', default=None,
                                               null=True, blank=True)

    def __str__(self):
        return self.nama
