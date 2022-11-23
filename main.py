from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re


with open('phonebook_raw.csv', mode='r', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=',')
    contacts_list = list(rows)
# print(contacts_list)

persons_list = {}
contacts_list_edited = [contacts_list[0]]

for row in contacts_list[1:]:

    # Задание 1
    name = re.split(r'\s', row[1])
    if len(name) > 1:
        row[2] = name[1]
    row[1] = name[0]
    name = re.split(r'\s', row[0])
    if len(name) > 1:
        row[1] = name[1]
    if len(name) > 2:
        row[2] = name[2]
    row[0] = name[0]

    #Задание 2
    # Приводим телефон с произвольной расстановкой скобок, пробелов и дефисов между цифрами
    # к формату +7(999)999-99-99

    pattern = r'(8|\+7)'+r'[\s)(-]*(\d)'*10 + r'\s*'
    row[5] = re.sub(pattern, r'+7(\2\3\4)\5\6\7-\8\9-\g<10>\g<11>', row[5])
    # Заменяем '  ( доб.  56 )   ' на ' доб. 56'
    row[5] = re.sub(r'[\s(]*доб\.\s*(\d+)[)\s]*', r' доб.\1', row[5], re.IGNORECASE)

    #Задание 3
    #Как было сказано на вебинаре, мы считаем человека одним и тем же, если совпадают имя и фамилия
    if (row[0], row[1]) not in persons_list:
        persons_list[(row[0], row[1])] = len(contacts_list_edited)
        contacts_list_edited.append(row)
    else:
        for index, value in enumerate(row):
            if value:
                contacts_list_edited[persons_list[(row[0], row[1])]][index] = value

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open('phonebook.csv', mode='w', encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONE)
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list_edited)

# pprint(contacts_list_edited)
