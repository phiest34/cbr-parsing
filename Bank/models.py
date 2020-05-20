from django.db import models
from dbfread import DBF
import sys
import csv


class banks(models.Model):
    name = models.CharField(max_length=10, default='none')


class bank_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=3, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=130, default='0', null=True)

    def __str__(self):
        return self.NAME_B


class bank_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)
    # chart = models.ImageField()


def load(request):
    tableS = DBF('E:/djangointerface/Bank/dbfiles/112019_123S.DBF', load=True, encoding="cp866")
    tableB = DBF('E:/djangointerface/Bank/dbfiles/112019_123B.DBF', load=True, encoding="cp866")
    bank = list()
    for record in range(len(tableS)):
        bank.append(bank_s.objects.get_or_create(REGN=tableS.records[record]['REGN'],
                                                    C1_S=tableS.records[record]['C1_S'],
                                                    C2_S=tableS.records[record]['C2_S'],
                                                    C31_S=tableS.records[record]['C31_S'],
                                                    C32_S=tableS.records[record]['C32_S']))

