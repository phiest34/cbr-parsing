import os
import matplotlib.pyplot as plt
import glob
from Bank.models import *
from Bank.do_not_open import decoding
import pandas as pd
from dbfread import DBF
from djangoInterface.settings import BASE_DIR

import datetime
from datetime import timedelta

extract = 'Bank/dbf_files/'


def formatting(month):
    """
    Автор: Молдатаев Нурсултан
    Цель: отформатировать строку для создания файла
    Вход: номер месяца
    Выход: номер месяца
    """
    if int(month) >= 10:
        return str(month)
    else:
        return '0' + str(month)


def get_key(dic, value):
    """
    Автор: Молдатаев Нурсултан
    Цель: получить ключ по значению из словаря
    Вход: словарь и значение
    Выход: ключ
    """
    for key, v in dic.items():
        if v == value:
            return key


def get_graph(bank: str, col: str):
    """
    Автор: Молдатаев Нурсултан
    Цель: построить график и сохранить
    Вход: название банка и номер показателя
    Выход: список с данными по показателю
    """

    def get_graph(bank: str, col: str):
        x_axis = []
        y_axis = []
        axes = []
        similar = set()
        regns = {}
        values = set()
        similar.clear()
        bank.lower()
        regns.clear()
        values.clear()
        regn = get_regn(bank)
        for file in glob.glob(extract + '*.rar'):
            dbfs = glob.glob(file + '/*.DBF')
            for dbf in dbfs:
                if dbf[-5] != 'B':
                    continue
                else:
                    table = DBF(dbf, load=True, encoding='cp866')
                    for record in table:
                        if record['NAME_B'].lower().find(bank) != -1:
                            similar.add(record['NAME_B'].lower())
                            regns[record['NAME_B'].lower()] = record['REGN']
                            values.add(record['REGN'])
        if len(values) == 1:
            for m in similar:
                regn = regns.get(m)
        bTable = {'C1_S', 'C2_S', 'C31_S', 'C32_S'}
        for file in glob.glob(extract + '*.rar'):
            dbfs = glob.glob(file + '/*.DBF')
            for dbf in dbfs:
                if dbf[-5] == 'D' and col in bTable or dbf[-5] != 'D' and dbf[-5] != 'B' and col not in bTable:
                    continue

                elif col not in bTable:
                    table = DBF(dbf, load=True, encoding='cp866')
                    found = False
                    for record in table:
                        if found or dbf[-5] != 'D':
                            break
                        if record['REGN'] == regn and record['C1'] == col:
                            y_axis.append(record['C3'])
                    if dbf[-5] == 'D':
                        continue
                    for record in table:
                        if record['REGN'] == regn:
                            try:
                                x_axis.append(record['DT'])
                                break
                            except Exception:
                                pass

                else:
                    table = DBF(dbf, load=True, encoding='cp866')

                    for record in table:
                        try:
                            if record['REGN'] == regn:
                                try:
                                    y_axis.append(record[col])
                                except Exception:
                                    pass
                                if len(y_axis):
                                    try:
                                        x_axis.append(record['DT'])
                                    except Exception:
                                        pass

                        except Exception:
                            pass
        f = plt.figure()
        if col in decoding:
            plt.title(decoding[col])
        else:
            plt.title(col)
        plt.grid()
        min_sl = min(len(x_axis), len(y_axis))
        x_axis = x_axis[:min_sl]
        y_axis = y_axis[:min_sl]
        f = plt.plot(x_axis, y_axis)
        plt.xlabel(bank)
        plt.savefig('Graphics/' + col + '_' + str(regn) + '.png')
        for i in range(min_sl):
            axes.append([])
            axes[i].append(str(x_axis[i]))
            axes[i].append(y_axis[i])
        return axes


def get_banks():
    """
    Автор: Молдатаев Нурсултан
    Цель: построить график и сохранить
    Вход: название банка и номер показателя
    Выход: список с данными по показателю
    """
    bank_string = ''
    for record in banks.objects.all():
        bank_string += str(record.name) + ', '
    bank_string = bank_string[:-2]
    return bank_string


def get_regn(bank: str):
    """
        Автор: Молдатаев Нурсултан
        Цель: получить регистрационный номер
        Вход: банк
        Выход: регистрационнный номер
        """
    for record in banks.objects.filter(name=bank):
        return int(record.REGN)


def month_report(date: str):
    """
        Автор: Селин Максим
        Цель: вывести отчетность в xls файле
        Вход: дата
        """
    cols = ['Название']
    df1 = pd.DataFrame(columns=['Расшифровка'])
    if date >= '2016-01-01':
        cols.append('C1_S')
        cols.append('C2_S')
        df1.loc['C1_S', 'Расшифровка'] = 'Объем акций и (или) субординированных облигаций финансовых ' \
                                         'организаций, отчужденных по сделкам РЕПО, тыс. руб.'
        df1.loc['C2_S', 'Расшифровка'] = 'Объем акций и (или) субординированных облигаций финансовых ' \
                                         'организаций, приобретенных по сделкам РЕПО, тыс. руб.'
    if date >= '2016-07-01':
        cols.append('C31_S')
        cols.append('C32_S')
        df1.loc['C31_S', 'Расшифровка'] = 'Финансовый результат по операциям с производными финансовыми' \
                                          ' инструментами, отраженный по строке 100.5 и (или) 101.9, ' \
                                          'и (или) 200.5 в составе финансового результата текущего ' \
                                          'года, включает:3.1. реализованный, тыс. руб.'
        df1.loc['C32_S', 'Расшифровка'] = 'Финансовый результат по операциям с производными финансовыми ' \
                                          'инструментами, отраженный по строке 100.5 и (или) 101.9, ' \
                                          'и (или) 200.5 в составе финансового результата текущего года, ' \
                                          'включает: 3.2. нереализованный, тыс. руб. '
    for record in banks_n.objects.filter(DT=date):
        cols.append(record.C1)
        df1.loc[record.C1, 'Расшифровка'] = record.C2_1 + record.C2_2 + record.C2_3
    df = pd.DataFrame(columns=cols)
    regns = set()

    for record in banks_d.objects.filter(DT=date):
        df.loc[record.REGN, record.C1] = record.C3
        regns.add(record.REGN)

    for record in banks_s.objects.filter(DT=date):
        df.loc[record.REGN, 'C1_S'] = record.C1_S
        df.loc[record.REGN, 'C2_S'] = record.C2_S
        df.loc[record.REGN, 'C31_S'] = record.C31_S
        df.loc[record.REGN, 'C32_S'] = record.C32_S

    for record in regns:
        for rec in banks.objects.filter(REGN=record):
            df.loc[record, 'Название'] = rec.name

    path = 'Output/' + date + '.xlsx'
    print(path)
    print(BASE_DIR)
    writer = pd.ExcelWriter(path)
    df.to_excel(writer, 'Banks')
    df1.to_excel(writer, 'Features')
    writer.save()


def get_months():
    """
        Автор: Селин Максим
        Цель: получить список всех месяцев
        Выход: список всех месяцев
        """
    months = []
    for file in os.listdir(extract):
        year = file[4:8]
        month = file[8:10]
        day = '01'
        months.append(year + '-' + month + '-' + day)
    return months


def bank_report(bank_name: str, year: int):
    """
            Автор: Селин Максим
            Цель: вывести отчетность в xls файле по бану за выбранный год
            Вход: год
            """
    regn = '0'
    for record in banks.objects.filter(name=bank_name):
        regn = record.REGN
    report_ld = datetime.datetime(year=year, month=12, day=1)
    report_fd = datetime.datetime(year=year, month=1, day=1)
    Data = []
    while report_ld - report_fd > timedelta(hours=1):

        df = pd.DataFrame(columns=['Наименование', 'Остаток'])
        report_fd += timedelta(days=28)
        date = str(report_fd.year) + '-' + formatting(report_fd.month) + '-01'
        name = ''
        for record in banks_s.objects.filter(DT=date, REGN=regn):
            if record.C1_S != '0':
                df.loc['C1_S', 'Остаток'] = record.C1_S
                df.loc['C1_S', 'Наименование'] = 'Объем акций и (или) субординированных облигаций финансовых ' \
                                                 'организаций, отчужденных по сделкам РЕПО, тыс. руб.'
            if record.C2_S != '0':
                df.loc['C2_S', 'Остаток'] = record.C2_S
                df.loc['C2_S', 'Наименование'] = 'Объем акций и (или) субординированных облигаций финансовых ' \
                                                 'организаций, приобретенных по сделкам РЕПО, тыс. руб.'
            if record.C31_S != '0':
                df.loc['C31_S', 'Остаток'] = record.C31_S
                df.loc['C31_S', 'Наименование'] = 'Финансовый результат по операциям с производными финансовыми' \
                                                  ' инструментами, отраженный по строке 100.5 и (или) 101.9, ' \
                                                  'и (или) 200.5 в составе финансового результата текущего ' \
                                                  'года, включает:3.1. реализованный, тыс. руб.'
            if record.C32_S != '0':
                df.loc['C32_S', 'Остаток'] = record.C32_S
                df.loc['C32_S', 'Наименование'] = 'Финансовый результат по операциям с производными финансовыми ' \
                                                  'инструментами, отраженный по строке 100.5 и (или) 101.9, ' \
                                                  'и (или) 200.5 в составе финансового результата текущего года, ' \
                                                  'включает: 3.2. нереализованный, тыс. руб. '
        for record in banks_d.objects.filter(DT=date, REGN=regn):
            if record.C3 != '0':
                for names in banks_n.objects.filter(DT=date, C1=record.C1):
                    name = names.C2_1 + names.C2_2 + names.C2_3
                df.loc[record.C1, 'Остаток'] = record.C3
                df.loc[record.C1, 'Наименование'] = name
        Data.append(df)

    path = 'Output/' + str(regn) + '_' + str(year) + '.xlsx'
    print(path)
    print(BASE_DIR)
    writer = pd.ExcelWriter(path)
    month = 0
    flag = False
    for i in Data:
        if len(i) > 0:
            flag = True
    if flag:
        for n, df in enumerate(Data):
            month += 1
            if len(df) == 0:
                continue
            df.to_excel(writer, '%s' % month)
        writer.save()
    return flag
