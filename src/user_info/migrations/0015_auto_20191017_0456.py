# Generated by Django 2.1.7 on 2019-10-17 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0014_personalkontak_hp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalkontak',
            name='hp',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='perusahaan',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_list', to='user_info.UserInfo'),
        ),
    ]
