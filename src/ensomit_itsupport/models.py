from django.db import models
from datetime import datetime

# Create your models here.


class SlaItsupport (models.Model):

    Analyst = 'AN'
    FieldEngineer = 'FE'
    FieldSupport = 'FS'

    CHOICES = (
                (Analyst, 'Analyst'),
                (FieldEngineer, 'Field Engineer'),
                (FieldSupport, 'Field Support'),
        )

    periode = models.CharField(
        'Periode',
        max_length=6
    )
    unit = models.CharField(
        'Unit',
        max_length=32
    )
    spesifikasi = models.CharField(
        'Spesifikasi',
        max_length=32,
        choices=CHOICES,
        default=FieldSupport
    )
    personil = models.CharField(
        'Personil',
        max_length=128
    )
    total_ticket = models.IntegerField(
        'Total Tiket',
        default=0
    )
    tiket_over_sla = models.IntegerField(
        'Tiket Over SLA',
        default=0
    )
    pencapaian_sla = models.DecimalField(
        'Pencapaian SLA (%)',
        default=0.0,
        max_digits=5,
        decimal_places=2
    )
    durasi_over = models.DecimalField(
        'Durasi Over (Hour)',
        default=0.0,
        max_digits=5,
        decimal_places=2
    )
    biaya_restitusi = models.DecimalField(
        'Biaya Restitusi (Rp)',
        default=0.0,
        max_digits=12,
        decimal_places=2
    )
    penempatan = models.CharField(
        'Penempatan',
        max_length=64
    )
    asman = models.CharField(
        'Asman',
        max_length=32
    )
    mulai_bekerja = models.DateField(
        'Mulai Bekerja',
        default=datetime.now
    )
    total_biaya = models.DecimalField(
        'Total Biaya (Rp)',
        default=0.0,
        max_digits=12,
        decimal_places=2
    )
