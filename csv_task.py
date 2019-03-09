
#Создайте список словарей:
#Запишите содержимое списка словарей в файл в формате csv

import csv
name_list = [
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]



with open('name_job.csv', 'w', encoding = 'utf-8', newline ='') as name_job:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(name_job, fields, delimiter=';')
    writer.writeheader()
    for name in name_list:
        writer.writerow(name)