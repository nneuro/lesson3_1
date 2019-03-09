import csv

with open('correlation_004_008.csv') as f:
    list_004_008 = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, delimiter=';', skipinitialspace=True)]
# print(list_004_008)
#{'gene': 'CYTB', '004 Control R_2016_10_19': '0.00184449660350928', 
# '008 Control R_2016_10_20': '0.0022030316508063', '': ''}



with open('correlation_other.csv') as f:
    list_other = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, delimiter=';', skipinitialspace=True)]
# print(list_other)

#{'gene': 'Chst7', '007 Control R_2017_06_27': '0.0000175987813147367',
#  '011 Control R_2017_06_30': '0.000031897', '011 mQ80 R_2018_02_27': '0.000014826069981746', 
# '008 MQ6h2 23.03 R_2018_04_27': '0.000028595',
#  '_009 MQ6_2 17.04 R_2018_04_27': '6.79264763819642E-06'}
genes_info = {}
for dict_1 in list_004_008:
    gene_expression = {
        '004 Control R_2016_10_19':dict_1['004 Control R_2016_10_19'],
        '008 Control R_2016_10_20':dict_1['008 Control R_2016_10_20']
        }
    gene_name = dict_1['gene']
    genes_info[gene_name] = gene_expression


for dict_2 in list_other:
    gene_expression_2 = {
        '007 Control R_2017_06_27':dict_2['007 Control R_2017_06_27'],
        '011 Control R_2017_06_30':dict_2['011 Control R_2017_06_30'],
        '011 mQ80 R_2018_02_27':dict_2['011 mQ80 R_2018_02_27'],
        '008 MQ6h2 23.03 R_2018_04_27':dict_2['008 MQ6h2 23.03 R_2018_04_27'],
        '_009 MQ6_2 17.04 R_2018_04_27':dict_2['_009 MQ6_2 17.04 R_2018_04_27'],
        }
    gene_name_2 = dict_2['gene']
    genes_info[gene_name_2] = genes_info.update(gene_expression_2)
print(genes_info)


# for genes_info['gene'] in genes_info_2:
#     genes_info['gene'].update(genes_info_2['gene'])
# print(genes_info)

'CYTB': {'004 Control R_2016_10_19': '0.00184449660350928',
 '008 Control R_2016_10_20': '0.0022030316508063'},
  '007 Control R_2017_06_27': '0.0000175987813147367',
   '011 Control R_2017_06_30': '0.000031897', 
   '011 mQ80 R_2018_02_27': '0.000014826069981746',
    '008 MQ6h2 23.03 R_2018_04_27': '0.000028595',
 '_009 MQ6_2 17.04 R_2018_04_27': '6.79264763819642E-06'}