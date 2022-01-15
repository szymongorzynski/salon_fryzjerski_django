# Generated by Django 4.0.1 on 2022-01-15 08:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicee',
            fields=[
                ('ServiceeId', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=40)),
                ('Price', models.IntegerField()),
                ('Time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('Email', models.EmailField(max_length=25, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('Pass', models.CharField(max_length=30)),
                ('Name', models.CharField(max_length=25)),
                ('LastName', models.CharField(max_length=25)),
                ('Phone', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('VisitId', models.AutoField(primary_key=True, serialize=False)),
                ('Ddate', models.DateField()),
                ('Hhour', models.TimeField()),
                ('Status', models.CharField(max_length=2)),
                ('ServiceeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fryzjer.servicee')),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fryzjer.user')),
            ],
        ),
    ]