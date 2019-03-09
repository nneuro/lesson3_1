#Задача: из двух csv-файлов, имеющих данные об экспрессии генов в разных образцах,
# собрать один, в котором будет показана экспрессия для общих генов (список генов в csv-файлах)

import csv

with open('correlation_004_008.csv') as f:   # Открываем первый файл с данными
    list_004_008 = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, delimiter=';', skipinitialspace=True)]

# print(list_004_008)
#{'gene': 'CYTB', '004 Control R_2016_10_19': '0.00184449660350928', 
# '008 Control R_2016_10_20': '0.0022030316508063', '': ''}



with open('correlation_other.csv') as f:     # Открываем файл с остальными данными
    list_other = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, delimiter=';', skipinitialspace=True)]
# print(list_other)

gene_list = []     #Создаём список с вложенными словарями, пригодный для превращения в csv
for el in list_004_008:
    for elem in list_other:
        if el['gene'] == elem['gene']:
            dict_new = {'gene': el['gene'],
            '004 Control R_2016_10_19': el['004 Control R_2016_10_19'],
            '008 Control R_2016_10_20': el['008 Control R_2016_10_20'],
            '007 Control R_2017_06_27': elem['007 Control R_2017_06_27'],
            '011 Control R_2017_06_30': elem['011 Control R_2017_06_30'],
            '011 mQ80 R_2018_02_27': elem['011 mQ80 R_2018_02_27'],
            '008 MQ6h2 23.03 R_2018_04_27': elem['008 MQ6h2 23.03 R_2018_04_27'],
            '_009 MQ6_2 17.04 R_2018_04_27': elem['_009 MQ6_2 17.04 R_2018_04_27']
            }
            # print(dict_new)
            gene_list.append(dict_new)
        else:
            continue  

# Создаём csv файл из полученного списка
with open('control_samples1.csv', 'w', encoding = 'utf-8', newline ='') as control_samples:
    fields = ['gene', 
    '004 Control R_2016_10_19', 
    '008 Control R_2016_10_20',
    '007 Control R_2017_06_27',
    '011 Control R_2017_06_30',
    '011 mQ80 R_2018_02_27',
    '008 MQ6h2 23.03 R_2018_04_27',
    '_009 MQ6_2 17.04 R_2018_04_27'
    ]
    writer = csv.DictWriter(control_samples, fields, delimiter=';')
    writer.writeheader()
    for gene in gene_list:
        writer.writerow(gene)



