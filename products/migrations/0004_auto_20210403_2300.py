# Generated by Django 3.1.4 on 2021-04-03 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_compp_pimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compp',
            name='Pimage',
            field=models.ImageField(null=True, upload_to='Product_pics'),
        ),
    ]
