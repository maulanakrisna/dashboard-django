# Generated by Django 3.2.1 on 2021-08-20 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0012_alter_network_sid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itsupport',
            old_name='sid',
            new_name='nik',
        ),
    ]
