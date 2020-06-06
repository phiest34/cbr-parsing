import time

import matplotlib.pyplot as plt
from djangoInterface.settings import BASE_DIR
from dbfread import DBF
import glob
import os

decoding = {'000': 'Суммарный капитал', 'C1_S': 'Объем акций отчужденных по сделкам',
            'C2_S': 'Объем акций приобретенных по сделкам',
            'C31_S': 'Финансовый результат по операциям, реализованный, тыс.руб', 'C32_S':
                'Финансовый результат по операциям, нереализованный, тыс.руб'}

regns = [0]


def formatting(month):
    if int(month) >= 10:
        return str(month)
    else:
        return '0' + str(month)


def get_key(dic, value):
    for key, v in dic.items():
        if v == value:
            return key


def get_graph(regn: int, col: str):
    start_time = time.time()
    extract = 'Bank/dbf_files/'
    x_axis = []
    y_axis = []

    similar = set()
    regns = {}
    values = set()
    similar.clear()
    bank = input()
    bank.lower()
    regns.clear()
    values.clear()
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
                        print(record['REGN'])
                        regns[record['NAME_B'].lower()] = record['REGN']
                        values.add(record['REGN'])

        print(*similar)
    if len(values) == 1:
        for m in similar:
            regn = regns.get(m)
            print('достали банк ', m, regn)
    else:
        return False

    bTable = {'C1_S', 'C2_S', 'C31_S', 'C32_S'}
    for file in glob.glob(extract + '*.rar'):
        dbfs = glob.glob(file + '/*.DBF')
        for dbf in dbfs:
            if dbf[-5] == 'D' and col in bTable or dbf[-5] != 'D' and dbf[-5] != 'B' and col not in bTable:
                continue

            elif col not in bTable:
                table = DBF(dbf, load=True, encoding='cp866')
                found = False
                loop = time.time()
                for record in table:
                    if found or dbf[-5] != 'D':
                        break
                    if record['REGN'] == regn and record['C1'] == col:
                        print('вошел')
                        y_axis.append(record['C3'])
                        print('положил', len(y_axis))
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

    print(len(x_axis))
    print(len(y_axis))
    if col in decoding:
        plt.title(decoding[col])
    else:
        plt.title(col)
    plt.grid()
    min_sl = min(len(x_axis), len(y_axis))
    plt.plot(x_axis[:min_sl], y_axis[:min_sl])
    plt.savefig(os.getcwd() + "/Work/Graphics/" + col + "_" + str(regn) + ".png")
    plt.show()
    return True
