import matplotlib.pyplot as plt
from djangoInterface.settings import BASE_DIR
from dbfread import DBF
import glob
import os


def formatting(month):
    if int(month) >= 10:
        return str(month)
    else:
        return '0' + str(month)


def get_graph(regn: int, col: str):
    extract = 'Bank/dbf_files/'
    x_axis = []
    y_axis = []
    decoding = {'C3': 'Суммарный капитал', 'C1_S': 'Объем акций отчужденных по сделкам',
                'C2_S': 'Объем акций приобретенных по сделкам',
                'C31_S': 'Финансовый результат по операциям, реализованный, тыс.руб', 'C32_S':
                    'Финансовый результат по операциям, нереализованный, тыс.руб'}

    for file in glob.glob(extract + '*.rar'):
        dbfs = glob.glob(file + '/*.DBF')
        for dbf in dbfs:
            if dbf[-5] == 'D' and col != 'C3' or dbf[-5] != 'D' and dbf[-5] != 'B' and col == 'C3':
                continue

            elif col == 'C3':
                table = DBF(dbf, load=True, encoding='cp866')
                found = False
                for record in table:
                    if found or dbf[-5] != 'D':
                        break
                    try:
                        if record['REGN'] == regn and record['C1'] == '000':
                            try:
                                y_axis.append(record[col])
                                found = True
                            except Exception:
                                pass
                    except Exception:
                        pass
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
    plt.title(decoding[col])
    plt.grid()
    min_sl = min(len(x_axis), len(y_axis))
    plt.plot(x_axis[:min_sl], y_axis[:min_sl])
    plt.savefig(os.path.join(BASE_DIR, '/Work/Graphics/' + col + "_" + str(regn) + ".png"))
    plt.show()
