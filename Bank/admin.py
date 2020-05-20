from django.contrib import admin
from Bank.models import banks
from Bank.models import bank_b
from Bank.models import bank_s

admin.site.register(banks)
admin.site.register(bank_b)
admin.site.register(bank_s)
