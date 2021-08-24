from django.db import models

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

    periode = models.DateField('Periode')
    unit = models.CharField(
        max_length=32
    )
    spesifikasi = models.CharField(
        max_length=32,
        choices=CHOICES,
        default=FieldSupport
    )
    personil = models.CharField(
        max_length=128
    )
    total_ticket = models.IntegerField()
    tiket_over_sla = models.IntegerField()
    pencapaian_sla = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    durasi_over = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    biaya_restitusi = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    penempatan = models.CharField(
        max_length=64
    )
    asman = models.CharField(
        max_length=32
    )
    mulai_bekerja = models.DateField()
    total_biaya = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
