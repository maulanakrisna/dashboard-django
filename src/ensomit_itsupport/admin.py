from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import SlaItsupport
from import_export.fields import Field
from import_export import widgets

# Register your models here.


class SlaItsupportResource(resources.ModelResource):
    periode = Field(attribute='periode', column_name='Periode')
    unit = Field(attribute='unit', column_name='Unit')
    spesifikasi = Field(attribute='spesifikasi', column_name='Spesifikasi')
    personil = Field(attribute='personil', column_name='Personil')
    total_ticket = Field(attribute='total_ticket',
                         column_name='Total Ticket')
    tiket_over_sla = Field(attribute='tiket_over_sla',
                           column_name='Tiket overSLA')
    pencapaian_sla = Field(attribute='pencapaian_sla',
                           column_name='Pencapaian SLA')
    durasi_over = Field(attribute='durasi_over',
                        column_name='Durasi over (Hour)')

    biaya_restitusi = Field(attribute='biaya_restitusi',
                            column_name='Biaya restitusi (Rp)')
    penempatan = Field(attribute='penempatan', column_name='Penempatan')
    asman = Field(attribute='asman', column_name='Asman')
    mulai_bekerja = Field(attribute='mulai_bekerja',
                          column_name='Mulai Bekerja')
    total_biaya = Field(attribute='total_biaya',
                        column_name='Total Biaya (Rp)')

    class Meta:
        model = SlaItsupport


class SlaItsupportAdmin(ImportExportModelAdmin):
    resource_class = SlaItsupportResource
    list_per_page = 10
    search_fields = ['periode', 'personil', 'unit', 'penempatan', 'asman']
    list_filter = ['spesifikasi', 'unit', 'asman', 'periode']
    list_display = ('periode', 'personil', 'total_ticket',
                    'pencapaian_sla', 'penempatan', 'total_biaya')


admin.site.register(SlaItsupport, SlaItsupportAdmin)
