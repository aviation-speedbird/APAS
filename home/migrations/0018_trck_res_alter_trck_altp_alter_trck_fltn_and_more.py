# Generated by Django 4.2.5 on 2023-10-11 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_trck_phno_alter_trck_altp_alter_trck_wi'),
    ]

    operations = [
        migrations.AddField(
            model_name='trck',
            name='res',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='trck',
            name='altp',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='trck',
            name='fltn',
            field=models.CharField(max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='trck',
            name='name',
            field=models.CharField(max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='trck',
            name='outtime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='trck',
            name='wi',
            field=models.IntegerField(null=True),
        ),
    ]
