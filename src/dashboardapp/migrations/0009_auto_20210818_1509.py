# Generated by Django 3.2.1 on 2021-08-18 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0008_address_province'),
    ]

    operations = [
        migrations.AlterField(
            model_name='network',
            name='ip_address',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='network',
            name='sid',
            field=models.CharField(max_length=32, unique=True, verbose_name='S I D'),
        ),
        migrations.AlterField(
            model_name='router',
            name='sid',
            field=models.CharField(max_length=32, unique=True, verbose_name='S I D'),
        ),
    ]
