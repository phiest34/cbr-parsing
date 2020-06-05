from django.shortcuts import render
import os
import datetime
from datetime import timedelta
from Bank.utils import *
from Bank.models import *

import rarfile
import wget
from dbfread import DBF


def index(request):
    return render(request, 'data/main.html')


def search_bank(request):
    try:
        bank_name = banks.objects.get(name=request.GET['bank_name'])
    except:
        return render(request, 'data/bank_not_found.html', {'test': request.GET['bank_name']})
    if (request.method == "GET") and ('bank_name' in request.GET) and (request.GET['bank_name'] == bank_name.name):
        return render(request, 'data/bank_found.html', {'test': request.GET['bank_name']})


def choice(request):
    results = request.GET["choices"]
    return render(request, 'data/second_main.html', {'choices': results})


def load(request):
    report = datetime.datetime(year=2014, month=1, day=1)
    current_date = datetime.datetime.now()

    directory = 'Bank/archives/'
    extract = 'Bank/dbf_files/'
    url = 'http://cbr.ru/vfs/credit/forms/'

    extract_list = os.listdir(extract)
    directory_list = os.listdir(directory)

    while current_date - report > timedelta(hours=1):
        report += timedelta(days=28)
        file = '123-' + str(report.year) + formatting(report.month) + '01.rar'
        try:
            if file not in directory_list:
                filename = wget.download(url + file)
                os.rename(filename, u'' + os.getcwd() + '/Bank/archives/' + filename)

            if file not in extract_list:
                rf = rarfile.RarFile(directory + file)
                rf.PATH_SEP = '/'
                path = os.path.join(extract, file)
                os.mkdir(path)
                rf.extractall(path=extract + file)

        except Exception:
            pass


    tableB = DBF('Bank/dbf_files/123-20140201.rar/012014_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20140201.rar/012014_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20140201.rar/012014_123N.DBF', load=True, encoding="cp866")

    if bank012014_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank012014_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank012014_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank012014_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank012014_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank012014_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20140301.rar/022014_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20140301.rar/022014_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20140301.rar/022014_123N.DBF', load=True, encoding="cp866")

    if bank022014_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank022014_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank022014_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank022014_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank022014_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank022014_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20140401.rar/032014_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20140401.rar/032014_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20140401.rar/032014_123N.DBF', load=True, encoding="cp866")

    if bank032014_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank032014_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank032014_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank032014_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank032014_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank032014_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20140501.rar/042014_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20140501.rar/042014_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20140501.rar/042014_123N.DBF', load=True, encoding="cp866")

    if bank042014_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank042014_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank042014_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank042014_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank042014_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank042014_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20140601.rar/052014_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20140601.rar/052014_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20140601.rar/052014_123N.DBF', load=True, encoding="cp866")

    if bank052014_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank052014_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank052014_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank052014_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank052014_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank052014_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20140701.rar/062014_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20140701.rar/062014_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20140701.rar/062014_123N.DBF', load=True, encoding="cp866")

    if bank062014_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank062014_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank062014_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank062014_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank062014_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank062014_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20140801.rar/072014_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20140801.rar/072014_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20140801.rar/072014_123N.DBF', load=True, encoding="cp866")

    if bank072014_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank072014_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank072014_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank072014_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank072014_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank072014_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20140901.rar/082014_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20140901.rar/082014_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20140901.rar/082014_123N.DBF', load=True, encoding="cp866")

    if bank082014_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank082014_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank082014_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank082014_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank082014_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank082014_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20141001.rar/092014_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20141001.rar/092014_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20141001.rar/092014_123N.DBF', load=True, encoding="cp866")

    if bank092014_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank092014_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank092014_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank092014_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank092014_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank092014_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20141101.rar/102014_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20141101.rar/102014_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20141101.rar/102014_123N.DBF', load=True, encoding="cp866")

    if bank102014_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank102014_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank102014_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank102014_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank102014_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank102014_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20141201.rar/112014_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20141201.rar/112014_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20141201.rar/112014_123N.DBF', load=True, encoding="cp866")

    if bank112014_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank112014_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank112014_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank112014_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank112014_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank112014_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20150101.rar/122014_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20150101.rar/122014_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20150101.rar/122014_123N.DBF', load=True, encoding="cp866")

    if bank122014_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank122014_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank122014_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank122014_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank122014_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank122014_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20150201.rar/012015_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20150201.rar/012015_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20150201.rar/012015_123N.DBF', load=True, encoding="cp866")

    if bank012015_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank012015_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank012015_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank012015_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank012015_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank012015_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20150301.rar/022015_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20150301.rar/022015_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20150301.rar/022015_123N.DBF', load=True, encoding="cp866")

    if bank022015_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank022015_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank022015_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank022015_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank022015_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank022015_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])



    ###########################################################################
    ###########################################################################
                                  #2015.02.01#
    ###########################################################################
    ###########################################################################

    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20190701.rar/062019_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20190701.rar/062019_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20190701.rar/062019_123N.DBF', load=True, encoding="cp866")
    tableS = DBF('Bank/dbf_files/123-20190701.rar/062019_123S.DBF', load=True, encoding="cp866")

    if bank062019_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank062019_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank062019_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank062019_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank062019_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank062019_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    if bank062019_s.objects.filter().count() != len(tableS):
        for record in range(len(tableS)):
            bank062019_s.objects.get_or_create(
                REGN=tableS.records[record]['REGN'],
                C1_S=tableS.records[record]['C1_S'],
                C2_S=tableS.records[record]['C2_S'],
                C31_S=tableS.records[record]['C31_S'],
                C32_S=tableS.records[record]['C32_S'],
            )

    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20190801.rar/072019_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20190801.rar/072019_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20190801.rar/072019_123N.DBF', load=True, encoding="cp866")
    tableS = DBF('Bank/dbf_files/123-20190801.rar/072019_123S.DBF', load=True, encoding="cp866")

    if bank072019_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank072019_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank072019_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank072019_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank072019_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank072019_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    if bank072019_s.objects.filter().count() != len(tableS):
        for record in range(len(tableS)):
            bank072019_s.objects.get_or_create(
                REGN=tableS.records[record]['REGN'],
                C1_S=tableS.records[record]['C1_S'],
                C2_S=tableS.records[record]['C2_S'],
                C31_S=tableS.records[record]['C31_S'],
                C32_S=tableS.records[record]['C32_S'],
            )

    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20190901.rar/082019_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20190901.rar/082019_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20190901.rar/082019_123N.DBF', load=True, encoding="cp866")
    tableS = DBF('Bank/dbf_files/123-20190901.rar/082019_123S.DBF', load=True, encoding="cp866")

    if bank082019_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank082019_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank082019_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank082019_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank082019_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank082019_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    if bank082019_s.objects.filter().count() != len(tableS):
        for record in range(len(tableS)):
            bank082019_s.objects.get_or_create(
                REGN=tableS.records[record]['REGN'],
                C1_S=tableS.records[record]['C1_S'],
                C2_S=tableS.records[record]['C2_S'],
                C31_S=tableS.records[record]['C31_S'],
                C32_S=tableS.records[record]['C32_S'],
            )


    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20191001.rar/092019_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20191001.rar/092019_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20191001.rar/092019_123N.DBF', load=True, encoding="cp866")
    tableS = DBF('Bank/dbf_files/123-20191001.rar/092019_123S.DBF', load=True, encoding="cp866")

    if bank092019_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank092019_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank092019_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank092019_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank092019_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank092019_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    if bank092019_s.objects.filter().count() != len(tableS):
        for record in range(len(tableS)):
            bank092019_s.objects.get_or_create(
                REGN=tableS.records[record]['REGN'],
                C1_S=tableS.records[record]['C1_S'],
                C2_S=tableS.records[record]['C2_S'],
                C31_S=tableS.records[record]['C31_S'],
                C32_S=tableS.records[record]['C32_S'],
            )

    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20191101.rar/102019_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20191101.rar/102019_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20191101.rar/102019_123N.DBF', load=True, encoding="cp866")
    tableS = DBF('Bank/dbf_files/123-20191101.rar/102019_123S.DBF', load=True, encoding="cp866")

    if bank102019_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank102019_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank102019_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank102019_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank102019_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank102019_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    if bank102019_s.objects.filter().count() != len(tableS):
        for record in range(len(tableS)):
            bank102019_s.objects.get_or_create(
                REGN=tableS.records[record]['REGN'],
                C1_S=tableS.records[record]['C1_S'],
                C2_S=tableS.records[record]['C2_S'],
                C31_S=tableS.records[record]['C31_S'],
                C32_S=tableS.records[record]['C32_S'],
            )

    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20191201.rar/112019_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20191201.rar/112019_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20191201.rar/112019_123N.DBF', load=True, encoding="cp866")
    tableS = DBF('Bank/dbf_files/123-20191201.rar/112019_123S.DBF', load=True, encoding="cp866")

    if bank112019_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank112019_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank112019_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank112019_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank112019_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank112019_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    if bank112019_s.objects.filter().count() != len(tableS):
        for record in range(len(tableS)):
            bank112019_s.objects.get_or_create(
                REGN=tableS.records[record]['REGN'],
                C1_S=tableS.records[record]['C1_S'],
                C2_S=tableS.records[record]['C2_S'],
                C31_S=tableS.records[record]['C31_S'],
                C32_S=tableS.records[record]['C32_S'],
            )

    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20200101.rar/122019_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20200101.rar/122019_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20200101.rar/122019_123N.DBF', load=True, encoding="cp866")
    tableS = DBF('Bank/dbf_files/123-20200101.rar/122019_123S.DBF', load=True, encoding="cp866")

    if bank122019_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank122019_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank122019_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank122019_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank122019_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank122019_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    if bank122019_s.objects.filter().count() != len(tableS):
        for record in range(len(tableS)):
            bank122019_s.objects.get_or_create(
                REGN=tableS.records[record]['REGN'],
                C1_S=tableS.records[record]['C1_S'],
                C2_S=tableS.records[record]['C2_S'],
                C31_S=tableS.records[record]['C31_S'],
                C32_S=tableS.records[record]['C32_S'],
            )

    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20200201.rar/012020_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20200201.rar/012020_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20200201.rar/012020_123N.DBF', load=True, encoding="cp866")
    tableS = DBF('Bank/dbf_files/123-20200201.rar/012020_123S.DBF', load=True, encoding="cp866")

    if bank012020_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank012020_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank012020_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank012020_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank012020_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank012020_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    if bank012020_s.objects.filter().count() != len(tableS):
        for record in range(len(tableS)):
            bank012020_s.objects.get_or_create(
                REGN=tableS.records[record]['REGN'],
                C1_S=tableS.records[record]['C1_S'],
                C2_S=tableS.records[record]['C2_S'],
                C31_S=tableS.records[record]['C31_S'],
                C32_S=tableS.records[record]['C32_S'],
            )

    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20200301.rar/022020_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20200301.rar/022020_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20200301.rar/022020_123N.DBF', load=True, encoding="cp866")
    tableS = DBF('Bank/dbf_files/123-20200301.rar/022020_123S.DBF', load=True, encoding="cp866")

    if bank022020_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank022020_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank022020_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank022020_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank022020_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank022020_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    if bank022020_s.objects.filter().count() != len(tableS):
        for record in range(len(tableS)):
            bank022020_s.objects.get_or_create(
                REGN=tableS.records[record]['REGN'],
                C1_S=tableS.records[record]['C1_S'],
                C2_S=tableS.records[record]['C2_S'],
                C31_S=tableS.records[record]['C31_S'],
                C32_S=tableS.records[record]['C32_S'],
            )

    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20200401.rar/032020_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20200401.rar/032020_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20200401.rar/032020_123N.DBF', load=True, encoding="cp866")
    tableS = DBF('Bank/dbf_files/123-20200401.rar/032020_123S.DBF', load=True, encoding="cp866")

    if bank032020_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank032020_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank032020_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank032020_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank032020_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank032020_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    if bank032020_s.objects.filter().count() != len(tableS):
        for record in range(len(tableS)):
            bank032020_s.objects.get_or_create(
                REGN=tableS.records[record]['REGN'],
                C1_S=tableS.records[record]['C1_S'],
                C2_S=tableS.records[record]['C2_S'],
                C31_S=tableS.records[record]['C31_S'],
                C32_S=tableS.records[record]['C32_S'],
            )

    ###########################################################################

    tableB = DBF('Bank/dbf_files/123-20200501.rar/042020_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/123-20200501.rar/042020_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/123-20200501.rar/042020_123N.DBF', load=True, encoding="cp866")
    tableS = DBF('Bank/dbf_files/123-20200501.rar/042020_123S.DBF', load=True, encoding="cp866")

    if bank042020_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank042020_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                               OKATO=tableB.records[record]['OKATO'],
                                               OKPO=tableB.records[record]['OKPO'],
                                               OGRN=tableB.records[record]['OGRN'],
                                               REGN_S=tableB.records[record]['REGN_S'],
                                               BIC=tableB.records[record]['BIC'],
                                               DT=tableB.records[record]['DT'],
                                               NAME_B=tableB.records[record]['NAME_B'],
                                               ADR=tableB.records[record]['ADR'])

    if bank042020_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank042020_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + ':' + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank042020_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank042020_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                               C2_1=tableN.records[record]['C2_1'],
                                               C2_2=tableN.records[record]['C2_2'],
                                               C2_3=tableN.records[record]['C2_3'])

    if bank042020_s.objects.filter().count() != len(tableS):
        for record in range(len(tableS)):
            bank042020_s.objects.get_or_create(
                REGN=tableS.records[record]['REGN'],
                C1_S=tableS.records[record]['C1_S'],
                C2_S=tableS.records[record]['C2_S'],
                C31_S=tableS.records[record]['C31_S'],
                C32_S=tableS.records[record]['C32_S'],
            )

    return render(request, 'data/main.html')
