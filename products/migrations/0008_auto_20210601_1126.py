# Generated by Django 3.1.4 on 2021-06-01 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_compp_pcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compp',
            name='Pcategory',
            field=models.CharField(default='Product Type', max_length=200),
        ),
    ]
