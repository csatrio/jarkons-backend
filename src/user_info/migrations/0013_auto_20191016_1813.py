# Generated by Django 2.1.7 on 2019-10-16 18:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0012_auto_20191015_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='KantorCabang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('alamat', models.CharField(max_length=255)),
                ('telepon', models.CharField(max_length=255)),
                ('fax', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Kantor Cabang',
                'verbose_name_plural': 'Kantor Cabang',
                'db_table': 'kantor_cabang',
            },
        ),
        migrations.CreateModel(
            name='PersonalKontak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('nama', models.CharField(max_length=255)),
                ('jabatan', models.CharField(max_length=255)),
                ('telepon', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('foto', models.ImageField(blank=True, default=None, null=True, upload_to='docs/personal_kontak/%Y/%m/%D/')),
            ],
            options={
                'verbose_name': 'Personal Kontak',
                'verbose_name_plural': 'Personal Kontak',
                'db_table': 'personal_kontak',
            },
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='kantor_cabang',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='tentang_perusahaan',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='personalkontak',
            name='perusahaan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='personal_kontak', to='user_info.UserInfo'),
        ),
        migrations.AddField(
            model_name='kantorcabang',
            name='perusahaan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='kantor_cabang', to='user_info.UserInfo'),
        ),
    ]
