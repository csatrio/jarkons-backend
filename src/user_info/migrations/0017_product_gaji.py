# Generated by Django 2.1.7 on 2019-10-17 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0016_auto_20191017_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gaji',
            field=models.DecimalField(blank=True, decimal_places=4, default=0, max_digits=20, null=True),
        ),
    ]