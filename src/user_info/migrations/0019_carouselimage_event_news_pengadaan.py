# Generated by Django 2.1.7 on 2019-10-17 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0018_auto_20191017_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('gambar', models.ImageField(blank=True, default=None, null=True, upload_to='docs/news/image/%Y/%m/%D/')),
            ],
            options={
                'verbose_name': 'Carousel Image',
                'verbose_name_plural': 'Carousel Image',
                'db_table': 'carousel_image',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('judul', models.CharField(max_length=255)),
                ('deskripsi_pendek', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('isi', models.TextField(blank=True, default=None, max_length=255, null=True)),
                ('info', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('lokasi', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('penyelenggara', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('link', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('tanggal_mulai', models.DateField()),
                ('tanggal_selesai', models.DateField()),
                ('gambar', models.ImageField(blank=True, default=None, null=True, upload_to='docs/events/image/%Y/%m/%D/')),
                ('thumbnail', models.ImageField(blank=True, default=None, null=True, upload_to='docs/events/thumbnail/%Y/%m/%D/')),
                ('perusahaan', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='event_list', to='user_info.UserInfo')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Event',
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('judul', models.CharField(max_length=255)),
                ('deskripsi_pendek', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('isi', models.TextField(blank=True, null=True)),
                ('gambar', models.ImageField(blank=True, default=None, null=True, upload_to='docs/news/image/%Y/%m/%D/')),
                ('thumbnail', models.ImageField(blank=True, default=None, null=True, upload_to='docs/news/thumbnail/%Y/%m/%D/')),
                ('perusahaan', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='news_list', to='user_info.UserInfo')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
                'db_table': 'news',
            },
        ),
        migrations.CreateModel(
            name='Pengadaan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('judul', models.CharField(max_length=255)),
                ('deskripsi_pendek', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('isi', models.TextField(blank=True, default=None, null=True)),
                ('batas_akhir_penawaran', models.DateField()),
                ('gambar', models.ImageField(blank=True, default=None, null=True, upload_to='docs/news/image/%Y/%m/%D/')),
                ('thumbnail', models.ImageField(blank=True, default=None, null=True, upload_to='docs/news/thumbnail/%Y/%m/%D/')),
                ('nomor_pengadaan', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('nama_pengadaan', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('nama_perusahaan_unit', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('nilai_hps_pagu', models.DecimalField(blank=True, decimal_places=4, default=0, max_digits=20, null=True)),
                ('lokasi_pengumuman', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('kategori_pengadaan', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('metode_pengadaan', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('kualifikasi_penyedia', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('link', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('perusahaan', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pengadaan_list', to='user_info.UserInfo')),
            ],
            options={
                'verbose_name': 'Pengadaan',
                'verbose_name_plural': 'Pengadaan',
                'db_table': 'pengadaan',
            },
        ),
    ]