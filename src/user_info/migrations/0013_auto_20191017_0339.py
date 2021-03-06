# Generated by Django 2.2.6 on 2019-10-17 03:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0012_auto_20191015_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='kantor_cabang',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gold_member',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='platinum_member',
            field=models.BooleanField(),
        ),
        migrations.CreateModel(
            name='InfoLoker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('nama_pekerjaan', models.CharField(max_length=255)),
                ('desc_pekerjaan', models.CharField(max_length=255)),
                ('lokasi', models.CharField(max_length=255)),
                ('gaji', models.CharField(max_length=255)),
                ('end_date', models.DateTimeField()),
                ('keahlian', models.TextField(null=True)),
                ('fasilitas', models.TextField(null=True)),
                ('kualifikasi', models.TextField(null=True)),
                ('perusahaan', models.ForeignKey(on_delete=django.db.models.deletion.SET, to='user_info.UserInfo')),
            ],
            options={
                'verbose_name': 'InfoLoker',
                'verbose_name_plural': 'InfoLoker',
                'db_table': 'info_loker',
            },
        ),
    ]
