# Generated by Django 3.2.1 on 2021-08-23 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0013_rename_sid_itsupport_nik'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itsupport',
            old_name='jobdescription',
            new_name='job_description',
        ),
        migrations.AlterField(
            model_name='itsupport',
            name='nik',
            field=models.CharField(max_length=32, verbose_name='N I K'),
        ),
    ]
