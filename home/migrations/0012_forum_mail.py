# Generated by Django 4.2.5 on 2023-10-07 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_forum_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='mail',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
