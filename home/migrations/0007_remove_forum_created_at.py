# Generated by Django 4.2.5 on 2023-10-07 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_contacts_forum_alter_snp_email_alter_snp_phno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='created_at',
        ),
    ]
