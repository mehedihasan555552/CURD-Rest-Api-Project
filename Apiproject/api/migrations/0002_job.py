# Generated by Django 3.0.6 on 2020-05-28 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('pay', models.CharField(max_length=200)),
                ('job_type', models.CharField(max_length=200)),
            ],
        ),
    ]