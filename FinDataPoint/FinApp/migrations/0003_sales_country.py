# Generated by Django 3.0 on 2022-06-21 11:10

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('FinApp', '0002_auto_20220621_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='Country',
            field=django_countries.fields.CountryField(max_length=45, null=True),
        ),
    ]
