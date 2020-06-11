from django.shortcuts import render
from Bank.scripts import *
from Bank.models import *
import rarfile
import wget
from dbfread import DBF
from Bank.fusioncharts import FusionCharts
from Bank.fusioncharts import FusionTable
from Bank.fusioncharts import TimeSeries
from Bank.do_not_open import decoding
import os


def chart(request):
    bank = forms.objects.last().data
    col = request.GET['col']
    key = get_key(decoding, col)
    data = get_graph(bank, key)
    if not data:
        return render(request, 'data/no_data.html', {'bank': bank})
    else:
        schema = [
            {
                "name": bank,
                "type": "date",
                "format": "%Y-%m-%d"
            },
            {
                "name": col,
                "type": "number"
            }
        ]

        fusionTable = FusionTable(schema, data)
        timeSeries = TimeSeries(fusionTable)

        timeSeries.AddAttribute("caption", {
            'text': bank
        })

        fcChart = FusionCharts("timeseries", "ex1", 800, 600,
                               "chart-1", "json", timeSeries)

        return render(request, 'data/graph.html', {'output': fcChart.render(), 'col_list': decoding.values()})


def index(request):
    return render(request, 'data/main.html')


def search_bank(request):
    try:
        bank_name = banks.objects.get(name=request.GET['bank_name'])
        if (request.method == "GET") and ('bank_name' in request.GET) and (request.GET['bank_name'] == bank_name.name):
            forms.objects.create(data=bank_name.name)
            return render(request, 'data/second_main.html',
                          {'bank': str(request.GET['bank_name']), 'col_list': decoding.values()})
    except Exception:
        return render(request, 'data/bank_not_found.html', {'bank': request.GET['bank_name']})


def choice(request):
    results = request.GET["choices"]
    bank_list = get_banks
    return render(request, 'data/second_main.html', {'choices': results, 'bank': '', 'bank_list': bank_list})


def load_data(request):
    print("load data")
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
    for file in glob.glob(extract + '*.rar'):
        dbfs = glob.glob(file + '/*.DBF')
        for dbf in dbfs:
            if dbf[-5] == 'B':
                table = DBF(dbf, load=True, encoding='cp866')
                for record in range(len(table)):
                    regn = table.records[record]['REGN']
                    name = table.records[record]['NAME_B']
                    pos = name.find(',')
                    if pos != -1:
                        name = name[:pos] + name[pos + 1:]
                    if banks.objects.filter(REGN=regn, name=name).count() > 0:
                        continue
                    elif banks.objects.filter(REGN=regn).count() > 0:
                        banks.objects.filter(REGN=regn).delete()
                    banks.objects.create(REGN=regn,
                                         name=name)

    return render(request, 'data/main.html')


def load_base(request):
    print("load base")
    extract = 'Bank/dbf_files/'
    for file in glob.glob(extract + '*.rar'):
        dbfs = glob.glob(file + '/*.DBF')
        for dbf in dbfs:
            table = DBF(dbf, load=True, encoding='cp866')
            date = dbf[-28:-24] + '-' + dbf[-24:-22] + '-' + dbf[-22:-20]
            # if dbf[-5] == 'B':
            #     if banks_b.objects.filter(DT=date).count() != len(table):
            #         banks_b.objects.filter(DT=date).delete()
            #         for record in range(len(table)):
            #             banks_b.objects.create(REGN=table.records[record]['REGN'],
            #                                    OKATO=table.records[record]['OKATO'],
            #                                    OKPO=table.records[record]['OKPO'],
            #                                    OGRN=table.records[record]['OGRN'],
            #                                    REGN_S=table.records[record]['REGN_S'],
            #                                    BIC=table.records[record]['BIC'],
            #                                    DT=table.records[record]['DT'],
            #                                    NAME_B=table.records[record]['NAME_B'],
            #                                    ADR=table.records[record]['ADR'])
            # if dbf[-5] == 'S':
            #     if banks_s.objects.filter(DT=date).count() != len(table):
            #         banks_s.objects.filter(DT=date).delete()
            #         if date > '2016-07-01':
            #             for record in range(len(table)):
            #                 banks_s.objects.create(DT=date,
            #                                        REGN=table.records[record]['REGN'],
            #                                        C1_S=table.records[record]['C1_S'],
            #                                        C2_S=table.records[record]['C2_S'],
            #                                        C31_S=table.records[record]['C31_S'],
            #                                        C32_S=table.records[record]['C32_S'])
            #         else:
            #             for record in range(len(table)):
            #                 banks_s.objects.create(DT=date,
            #                                        REGN=table.records[record]['REGN'],
            #                                        C1_S=table.records[record]['C1_S'],
            #                                        C2_S=table.records[record]['C2_S'])
            # if dbf[-5] == 'N':
            #     if banks_n.objects.filter(DT=date).count() != len(table):
            #         banks_n.objects.filter(DT=date).delete()
            #         for record in range(len(table)):
            #             banks_n.objects.create(DT=date,
            #                                    C1=table.records[record]['C1'],
            #                                    C2_1=table.records[record]['C2_1'],
            #                                    C2_2=table.records[record]['C2_2'],
            #                                    C2_3=table.records[record]['C2_3'])
            # if dbf[-5] == 'D' and date == '2020-05-01':
            #     if banks_d.objects.filter(DT=date).count() != len(table):
            #         banks_d.objects.filter(DT=date).delete()
            #         for record in range(len(table)):
            #             banks_d.objects.create(DT=date,
            #                                    REGN=table.records[record]['REGN'],
            #                                    C1=table.records[record]['C1'],
            #                                    C3=table.records[record]['C3'])

    return render(request, 'data/main.html')


def report_by_date(request):
    date = request.GET['date']
    month_report(date)
    return render(request, 'data/main.html')


def text_choice(request):
    results = request.GET["text_choices"]
    months = get_months()
    bank_list = get_banks
    return render(request, 'data/second_main.html',
                  {'text_choices': results, 'bank': '', 'months': months, 'bank_list': bank_list})


def report_by_bank(request):
    bank = request.GET["bank"]
    year = int(request.GET["year"])
    print(year)
    print(bank)
    if bank_report(bank, year):
        return render(request, 'data/main.html')
    else:
        return render(request, 'data/no_data.html', {'bank': bank})
