# Generated by Django 4.0.1 on 2022-01-25 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fryzjer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='UserId',
            field=models.CharField(default=None, max_length=5),
        ),
    ]