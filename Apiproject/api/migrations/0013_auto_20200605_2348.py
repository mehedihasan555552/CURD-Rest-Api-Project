# Generated by Django 3.0.6 on 2020-06-05 17:48

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20200605_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='specializes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=15), blank=True, null=True, size=None),
        ),
    ]