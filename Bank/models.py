from django.db import models
from django.http import HttpResponse
import sys
import csv


class banks(models.Model):
    name = models.CharField(max_length=110, default='none')

    def __str__(self):
        return self.name


###################################################################
###################################################################
###################################################################
###################################################################
###################################################################

class forms(models.Model):
    data = models.CharField(max_length=100, default='0', null=True)

    def __str__(self):
        return self.data


class bank012014_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank012014_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank012014_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank022014_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank022014_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank022014_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank032014_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank032014_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank032014_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank042014_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank042014_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank042014_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank052014_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank052014_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank052014_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank062014_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank062014_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank062014_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank072014_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank072014_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank072014_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank082014_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank082014_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank082014_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank092014_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank092014_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank092014_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank102014_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank102014_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank102014_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank112014_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank112014_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank112014_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank122014_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank122014_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank122014_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


###################################################################
###################################################################
###################################################################
###################################################################
###################################################################


class bank012015_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank012015_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank012015_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank022015_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank022015_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank022015_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank032015_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank032015_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank032015_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank042015_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank042015_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank042015_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank052015_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank052015_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank052015_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank062015_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank062015_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank062015_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank072015_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank072015_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank072015_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank082015_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank082015_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank082015_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank092015_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank092015_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank092015_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank102015_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank102015_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank102015_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank112015_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank112015_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank112015_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank122015_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank122015_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank122015_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


###################################################################
###################################################################
###################################################################
###################################################################
###################################################################

class bank012016_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank012016_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)


class bank012016_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank012016_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank022016_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank022016_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank022016_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)


class bank022016_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank032016_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank032016_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank032016_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank032016_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)


class bank042016_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank042016_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank042016_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)


class bank042016_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank052016_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank052016_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank052016_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)


class bank052016_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank062016_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank062016_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank062016_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)


class bank062016_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank072016_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank072016_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank072016_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)


class bank072016_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank082016_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank082016_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank082016_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank082016_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank092016_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank092016_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank092016_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank092016_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank102016_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank102016_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank102016_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank102016_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank112016_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank112016_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank112016_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank112016_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank122016_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank122016_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank122016_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank122016_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


###################################################################
###################################################################
###################################################################
###################################################################
###################################################################

class bank012017_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank012017_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank012017_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank012017_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank022017_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank022017_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank022017_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank022017_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank032017_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank032017_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank032017_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank032017_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank042017_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank042017_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank042017_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank042017_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank052017_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank052017_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank052017_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank052017_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank062017_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank062017_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank062017_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank062017_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank072017_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank072017_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank072017_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank072017_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank082017_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank082017_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank082017_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank082017_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank092017_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank092017_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank092017_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank092017_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank102017_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank102017_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank102017_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank102017_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank112017_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank112017_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank112017_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank112017_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank122017_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank122017_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank122017_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank122017_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


###################################################################
###################################################################
###################################################################
###################################################################
###################################################################

class bank012018_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank012018_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank012018_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank012018_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank022018_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank022018_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank022018_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank022018_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank032018_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank032018_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank032018_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank032018_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank042018_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank042018_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank042018_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank042018_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank052018_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank052018_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank052018_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank052018_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank062018_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank062018_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank062018_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank062018_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank072018_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank072018_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank072018_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank072018_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank082018_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank082018_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank082018_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank082018_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank092018_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank092018_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank092018_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank092018_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank102018_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank102018_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank102018_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank102018_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank112018_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank112018_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank112018_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank112018_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank122018_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank122018_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank122018_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank122018_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


###################################################################
###################################################################
###################################################################
###################################################################
###################################################################

class bank012019_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank012019_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank012019_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank012019_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank022019_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank022019_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank022019_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank022019_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank032019_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank032019_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank032019_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank032019_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank042019_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank042019_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank042019_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank042019_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank052019_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank052019_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank052019_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank052019_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank062019_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank062019_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank062019_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank062019_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank072019_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank072019_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank072019_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank072019_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank082019_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank082019_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank082019_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank082019_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank092019_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank092019_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank092019_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank092019_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank102019_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank102019_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank102019_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank102019_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank112019_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank112019_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank112019_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank112019_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank122019_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank122019_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank122019_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank122019_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


###################################################################
###################################################################
###################################################################
###################################################################
###################################################################

class bank012020_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank012020_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank012020_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank012020_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank022020_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank022020_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank022020_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank022020_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank032020_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank032020_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank032020_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank032020_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank042020_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank042020_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank042020_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank042020_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank052020_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)


class bank052020_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank052020_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)


class bank052020_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)


class bank_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)
    # chart = models.ImageField()
