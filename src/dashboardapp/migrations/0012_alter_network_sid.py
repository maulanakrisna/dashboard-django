# Generated by Django 3.2.1 on 2021-08-19 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0011_remove_office_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='network',
            name='sid',
            field=models.CharField(max_length=11, unique=True, verbose_name='S I D'),
        ),
    ]
