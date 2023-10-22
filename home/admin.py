from django.contrib import admin
from .models import Contacts, trck
from .models import snp, forum, prk, event, alert

# Register your models here.
admin.site.register(Contacts)
admin.site.register(snp)
admin.site.register(forum)
admin.site.register(prk)
admin.site.register(event)
admin.site.register(trck)
admin.site.register(alert)