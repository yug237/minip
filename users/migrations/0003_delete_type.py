# Generated by Django 3.1.4 on 2021-04-06 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Type',
        ),
    ]
