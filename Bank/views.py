from django.shortcuts import render
from Bank.models import bank_s
from Bank.models import bank_b
from Bank.models import bank_d
from Bank.models import banks
from Bank.models import bank_n
import datetime
import rarfile
import wget
import os
from dbfread import DBF


def formatting(month):
    if int(month) >= 10:
        return str(month)
    else:
        return '0' + str(month)


def index(request):
    return render(request, 'data/main.html')


def search_bank(request):
    try:
        bank_name = banks.objects.get(name=request.GET['bank_name'])
    except:
        return render(request, 'data/bank_not_found.html', {'test': request.GET['bank_name']})
    if (request.method == "GET") and ('bank_name' in request.GET) and (request.GET['bank_name'] == bank_name.title):
        return render(request, 'data/bank_found.html', {'test': request.GET['bank_name']})


def choice(request):
    results = request.GET["choices"]
    return render(request, 'data/second_main.html', {'choices': results})


def load(request):
    report = datetime.datetime(year=2020, month=4, day=1)
    current_date = datetime.datetime.now()
    directory = 'Bank/archives/'
    extract = 'Bank/dbf_files/'
    extract_list = os.listdir(extract)
    while report.month < current_date.month:
        report = report.replace(month=report.month + 1)
        file = '123-' + str(report.year) + formatting(report.month) + '01.rar'
        try:
            filename = wget.download('http://old.cbr.ru/vfs/credit/forms/' + file)
            os.rename(filename, u'' + os.getcwd() + '/Bank/archives/' + filename)
            if file not in extract_list:
                rf = rarfile.RarFile(directory + file)
                rf.PATH_SEP = '/'
                path = os.path.join(extract, file)
                os.mkdir(path)
                rf.extractall(path=extract + file)
        except:
            pass

    tableS = DBF('Bank/dbf_files/112019_123S.DBF', load=True, encoding="cp866")
    tableB = DBF('Bank/dbf_files/112019_123B.DBF', load=True, encoding="cp866")
    tableD = DBF('Bank/dbf_files/112019_123D.DBF', load=True, encoding="cp866")
    tableN = DBF('Bank/dbf_files/112019_123N.DBF', load=True, encoding="cp866")
    if bank_s.objects.count() != len(tableN):
        for record in range(len(tableS)):
            bank_s.objects.get_or_create(REGN=tableS.records[record]['REGN'],
                                         C1_S=tableS.records[record]['C1_S'],
                                         C31_S=tableS.records[record]['C31_S'],
                                         C2_S=tableS.records[record]['C2_S'],
                                         C32_S=tableS.records[record]['C32_S'])

    if bank_b.objects.filter().count() != len(tableB):
        for record in range(len(tableB)):
            bank_b.objects.get_or_create(REGN=tableB.records[record]['REGN'],
                                         OKATO=tableB.records[record]['OKATO'],
                                         OKPO=tableB.records[record]['OKPO'],
                                         OGRN=tableB.records[record]['OGRN'],
                                         REGN_S=tableB.records[record]['REGN_S'],
                                         BIC=tableB.records[record]['BIC'],
                                         DT=tableB.records[record]['DT'],
                                         NAME_B=tableB.records[record]['NAME_B'],
                                         ADR=tableB.records[record]['ADR'])

    if bank_d.objects.filter().count() != len(tableD):
        for record in range(len(tableD)):
            bank_d.objects.get_or_create(
                REGN_C1=str(tableD.records[record]['REGN']) + str(tableD.records[record]['C1']),
                C3=tableD.records[record]['C3'])

    if bank_n.objects.filter().count() != len(tableN):
        for record in range(len(tableN)):
            bank_n.objects.get_or_create(C1=tableN.records[record]['C1'],
                                         C2_1=tableN.records[record]['C2_1'],
                                         C2_2=tableN.records[record]['C2_2'],
                                         C2_3=tableN.records[record]['C2_3'])
    return render(request, 'data/main.html')
