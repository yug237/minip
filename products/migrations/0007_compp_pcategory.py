# Generated by Django 3.1.4 on 2021-05-31 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_compp_pprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='compp',
            name='Pcategory',
            field=models.CharField(default='Random', max_length=200),
        ),
    ]
