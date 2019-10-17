import django_mysql
from django.conf import settings
from django.db import models
from common.models import BaseModel


class Profesi(BaseModel):
    class Meta:
        db_table = 'profesi'
        verbose_name = 'Profesi'
        verbose_name_plural = 'Profesi'

    is_automatic_admin = False
    optimize_select_related = False
    serialize_list = False
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Provinsi(BaseModel):
    class Meta:
        db_table = 'provinsi'
        verbose_name = 'Provinsi'
        verbose_name_plural = 'Provinsi'

    optimize_select_related = False
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class KabupatenKota(BaseModel):
    class Meta:
        db_table = 'kabupaten_kota'
        verbose_name = 'Kabupaten Kota'
        verbose_name_plural = 'Kabupaten Kota'

    optimize_select_related = False
    text = models.CharField(max_length=255)
    provinsi = models.ForeignKey(Provinsi, related_name='kabupaten_list', on_delete=models.DO_NOTHING, default=None)

    def __str__(self):
        return self.text


class Keahlian(BaseModel):
    class Meta:
        db_table = 'keahlian'
        verbose_name = 'keahlian'
        verbose_name_plural = 'keahlian'

    is_automatic_admin = False
    optimize_select_related = False
    text = models.CharField(max_length=255)
    profesi = models.ForeignKey(Profesi, related_name='keahlian_list', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.text


class Klasifikasi(BaseModel):
    class Meta:
        db_table = 'klasifikasi'
        verbose_name = 'Klasifikasi'
        verbose_name_plural = 'Klasifikasi'

    is_automatic_admin = False
    optimize_select_related = False
    text = models.CharField(max_length=255)
    profesi = models.ForeignKey(Profesi, related_name='klasifikasi_list', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.text


class Kualifikasi(BaseModel):
    class Meta:
        db_table = 'kualifikasi'
        verbose_name = 'Kualifikasi'
        verbose_name_plural = 'Kualifikasi'

    is_automatic_admin = False
    optimize_select_related = False
    text = models.CharField(max_length=255)
    profesi = models.ForeignKey(Profesi, related_name='kualifikasi_list', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.text


class PengalamanKerja(BaseModel):
    class Meta:
        db_table = 'pengalaman_kerja'
        verbose_name = 'Pengalaman Kerja'
        verbose_name_plural = 'Pengalaman Kerja'

    optimize_select_related = False
    user_info = models.ForeignKey('UserInfo', related_name='pengalaman_kerja', on_delete=models.DO_NOTHING)
    uraian_pekerjaan = models.TextField(null=True, blank=True)
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


class Lowongan(BaseModel):
    class Meta:
        db_table = 'lowongan'
        verbose_name = 'Lowongan'
        verbose_name_plural = 'Lowongan'

    posisi = models.CharField(max_length=255)
    perusahaan = models.ForeignKey('UserInfo', related_name='lowongan_list', on_delete=models.DO_NOTHING)
    deskripsi = models.TextField(null=True, blank=True)
    berakhir_pada = models.DateField()


class UserInfo(BaseModel):
    class Meta:
        db_table = 'user_info'
        verbose_name = 'User Info'
        verbose_name_plural = 'Users Info'

    optimize_select_related = False

    gold_member = models.BooleanField(default=False)
    platinum_member = models.BooleanField(default=False)
    bersedia_mengirim_ke_lokasi_pekerjaan = models.BooleanField(default=False)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='info', on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    no_telepon = models.CharField(max_length=255, null=True, blank=True)
    profesi = models.ForeignKey(Profesi, on_delete=models.DO_NOTHING)
    nama_perusahaan = models.CharField(max_length=255)
    jabatan_di_perusahaan = models.CharField(max_length=255)
    alamat_perusahaan = models.CharField(max_length=255)
    gold_member = models.BooleanField(blank=False,null=False)
    platinum_member = models.BooleanField(blank=False, null=False)
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
    logo_perusahaan = models.ImageField(upload_to=f"docs/logo_perusahaan/%Y/%m/%D/", default=None,
                                        null=True, blank=True)
    selfie_dengan_identitas_diri = models.ImageField(upload_to=f"docs/selfie_dengan_identitas_diri/%Y/%m/%D/",
                                                     default=None,
                                                     null=True, blank=True)

    masalah_yang_sering_dihadapi = models.TextField(null=True, blank=True)
    bantuan_yang_dibutuhkan = models.TextField(null=True, blank=True)
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

    # company detail
    kantor_cabang = models.TextField(null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    rating = models.IntegerField(default=3)

    def __str__(self):
        return self.nama


class Product(BaseModel):
    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Product'

    optimize_select_related = False

    nama_produk = models.CharField(max_length=255)
    gambar = models.ImageField(upload_to=f"docs/produk/%Y/%m/%D/", default=None, null=True, blank=True)
    perusahaan = models.ForeignKey(UserInfo, related_name='product_list', on_delete=models.DO_NOTHING)
    deskripsi = models.TextField(null=True, blank=True)


class InfoLoker(BaseModel):
    class Meta:
        db_table = 'info_loker'
        verbose_name = 'InfoLoker'
        verbose_name_plural = 'InfoLoker'

    optimize_select_related = False
    nama_pekerjaan = models.CharField(max_length=255)
    desc_pekerjaan = models.CharField(max_length=255)
    lokasi = models.CharField(max_length=255)
    # perusahaan_id = models.IntegerField(null=False)
    perusahaan = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING)
    gaji = models.CharField(max_length=255)
    end_date = models.DateTimeField(null=False)
    keahlian = models.TextField(null=True)
    fasilitas = models.TextField(null=True)
    kualifikasi = models.TextField(null=True)

