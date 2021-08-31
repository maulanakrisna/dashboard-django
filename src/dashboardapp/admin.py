from django.contrib import admin

from .models import Sti, Address, Office, Router, Network, Computer, Itsupport


class RouterAdmin(admin.ModelAdmin):
    list_display = ('sid', 'type', 'brand', 'model', 'office')
    list_filter = ['brand', 'type', 'model']
    search_fields = ['sid', 'type', 'brand', 'model']
    list_per_page = 10


class NetworkAdmin(admin.ModelAdmin):
    list_display = ('sid', 'office', 'type', 'bandwidth', 'act_date')
    list_filter = ['bandwidth', 'type', 'office']
    search_fields = ['sid', 'type', 'ip_address']
    list_per_page = 10


class OfficeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'sti']
    list_per_page = 10
    list_filter = ['sti']


class AddressAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['office', 'address1', 'city', 'province']
    list_per_page = 10
    list_filter = ['province', 'city']


class ItsupportAdmin(admin.ModelAdmin):
    search_fields = ['name', 'nik']
    list_display = ['nik', 'name', 'office']
    list_per_page = 10
    list_filter = ['job_description', 'office']


admin.site.register(Sti)
admin.site.register(Address, AddressAdmin)
admin.site.register(Office, OfficeAdmin)
admin.site.register(Router, RouterAdmin)
admin.site.register(Network, NetworkAdmin)
admin.site.register(Computer)
admin.site.register(Itsupport, ItsupportAdmin)
