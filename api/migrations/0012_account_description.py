# Generated by Django 3.0.6 on 2020-06-05 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_account_passwrod'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]