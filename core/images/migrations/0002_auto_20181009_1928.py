# Generated by Django 2.1.2 on 2018-10-09 19:28

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='latitude',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='longitude',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
