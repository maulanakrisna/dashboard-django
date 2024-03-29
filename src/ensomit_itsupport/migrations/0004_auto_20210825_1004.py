# Generated by Django 3.2.6 on 2021-08-25 02:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ensomit_itsupport', '0003_alter_slaitsupport_total_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slaitsupport',
            name='biaya_restitusi',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='slaitsupport',
            name='durasi_over',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='slaitsupport',
            name='mulai_bekerja',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='slaitsupport',
            name='pencapaian_sla',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='slaitsupport',
            name='tiket_over_sla',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='slaitsupport',
            name='total_biaya',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='slaitsupport',
            name='total_ticket',
            field=models.IntegerField(default=0),
        ),
    ]
