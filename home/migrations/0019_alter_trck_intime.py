# Generated by Django 4.2.5 on 2023-10-11 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_trck_res_alter_trck_altp_alter_trck_fltn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trck',
            name='intime',
            field=models.DateTimeField(null=True),
        ),
    ]
