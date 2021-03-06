# Generated by Django 3.1.4 on 2021-04-08 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_interest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='interest',
            name='choice',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='interest',
            name='gender',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='interest',
            name='occupation',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
