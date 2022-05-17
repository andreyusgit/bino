from openpyxl import load_workbook
import math

positive = []  # создаем список со значениями х при которых зачет сдан
negative = []  # при этих значениях х зачет не сдан
averP = 0
averN = 0


# функция, которая импортирует все значения из таблицы в списки
def imp():
    global averP
    global averN
    data = load_workbook("data.xlsx")
    sheet = data['Sheet1']
    rows = sheet.max_row
    for index in range(2, rows):
        if sheet[f'B{index}'].value == 'да':
            averP += int(sheet[f'A{index}'].value)
            positive.append(sheet[f'A{index}'].value)
        elif sheet[f'B{index}'].value == 'нет':
            averN += int(sheet[f'A{index}'].value)
            negative.append(sheet[f'A{index}'].value)


# логистическая функция
def func(x):
    return (math.exp(-7 + x)) / (1 + math.exp(-7 + x))


# в этой функции происходит сравнение переданного в функцию значения и К.З.
def artificial_result(cv, x):
    if func(x) >= cv:
        return 'зачет'
    else:
        return 'незачет'


def main():
    imp()
    control_value = func(int(((averP / len(positive)) + (averN / len(negative))) / 2))
    return control_value
