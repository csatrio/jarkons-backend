# Generated by Django 2.1.7 on 2019-10-17 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0015_auto_20191017_0456'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='fasilitas',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='keahlian',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='kualifikasi',
            field=models.TextField(blank=True, null=True),
        ),
    ]
