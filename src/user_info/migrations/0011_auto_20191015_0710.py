# Generated by Django 2.1.7 on 2019-10-15 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0010_auto_20191011_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='gold_member',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='platinum_member',
            field=models.BooleanField(default=False),
        ),
    ]
