from django.contrib import admin

from .models import Sti, Address, Office, Router, Network, Computer, Itsupport

admin.site.register(Sti)
admin.site.register(Address)
admin.site.register(Office)
admin.site.register(Router)
admin.site.register(Network)
admin.site.register(Computer)
admin.site.register(Itsupport)
