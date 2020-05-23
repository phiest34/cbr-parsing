from django.db import models
from django.http import HttpResponse
import sys
import csv


class banks(models.Model):
    name = models.CharField(max_length=10, default='none')


class bank_b(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    OKATO = models.CharField(max_length=2, default='0', null=True)
    OKPO = models.CharField(max_length=8, default='0', null=True)
    OGRN = models.CharField(max_length=13, default='0', null=True)
    REGN_S = models.CharField(max_length=10, default='0', null=True)
    BIC = models.CharField(max_length=9, default='0', null=True)
    DT = models.CharField(max_length=10, default='0', null=True)
    NAME_B = models.CharField(max_length=60, default='0', null=True)
    ADR = models.CharField(max_length=200, default='0', null=True)

    def __str__(self):
        return self.NAME_B


class bank_s(models.Model):
    REGN = models.CharField(max_length=10, default='0', primary_key=True)
    C1_S = models.CharField(max_length=20, default='0', null=True)
    C2_S = models.CharField(max_length=20, default='0', null=True)
    C31_S = models.CharField(max_length=20, default='0', null=True)
    C32_S = models.CharField(max_length=20, default='0', null=True)
    # chart = models.ImageField()


class bank_d(models.Model):
    # REGN = models.CharField(max_length=10, default='0', null=True)
    # C1 = models.CharField(max_length=30, default='0', primary_key=True)
    REGN_C1 = models.CharField(max_length=40, default='0', primary_key=True)
    C3 = models.CharField(max_length=30, default='0', null=True)


class bank_n(models.Model):
    C1 = models.CharField(max_length=11, default='0', primary_key=True)
    C2_1 = models.CharField(max_length=240, default='0', null=True)
    C2_2 = models.CharField(max_length=240, default='0', null=True)
    C2_3 = models.CharField(max_length=70, default='0', null=True)
