# Generated by Django 4.0.1 on 2022-01-18 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fryzjer', '0005_rename_serviceeid_visit_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visit',
            old_name='Service',
            new_name='Servicee',
        ),
    ]