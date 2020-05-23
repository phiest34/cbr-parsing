from django.contrib import admin
from Bank.models import banks
from Bank.models import bank_b
from Bank.models import bank_s
from Bank.models import bank_d
from Bank.models import bank_n

admin.site.register(banks)
admin.site.register(bank_b)
admin.site.register(bank_s)
admin.site.register(bank_d)
admin.site.register(bank_n)

