# Generated by Django 4.2.5 on 2023-10-21 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_alter_trck_wi'),
    ]

    operations = [
        migrations.AddField(
            model_name='snp',
            name='priv',
            field=models.IntegerField(default=0, max_length=10, null=True),
        ),
    ]