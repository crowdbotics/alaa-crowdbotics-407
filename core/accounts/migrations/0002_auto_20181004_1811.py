# Generated by Django 2.1.2 on 2018-10-04 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('N', 'Not specified'), ('M', 'Male')], default='N', max_length=1),
        ),
    ]