from openpyxl import load_workbook
import math
from array import *
import numpy as np
from numpy import linalg

positive = array('B', [])  # создаем массив со значениями х при которых зачет сдан
negative = array('B', [])  # при этих значениях х зачет не сдан
averP = 0
averN = 0
a0 = 0
a1 = 0


# функция, которая импортирует все значения из таблицы в списки
def imp():
    global averP
    global averN
    data = load_workbook("data.xlsx")
    sheet = data['Sheet1']
    rows = sheet.max_row
    for index in range(2, rows + 1):
        if sheet[f'B{index}'].value == 'да':
            averP += int(sheet[f'A{index}'].value)
            positive.append(sheet[f'A{index}'].value)
        elif sheet[f'B{index}'].value == 'нет':
            averN += int(sheet[f'A{index}'].value)
            negative.append(sheet[f'A{index}'].value)
    square_method(False)
    square_method(True)


def square_method(check):
    global a0
    global a1
    P = np.array([[0.88]*2 for i in range(len(positive) + len(negative))])
    Y = np.array([[0] * 1 for i in range(len(positive) + len(negative))])
    W = np.array([[0.88] * (len(positive) + len(negative)) for i in range(len(positive) + len(negative))])
    data = load_workbook("data.xlsx")
    sheet = data['Sheet1']
    for i in range(2, len(positive) + len(negative) + 2):
        for j in range(2):
            if j % 2 == 0:
                P[i - 2][j] = 1
            else:
                P[i - 2][j] = xs(sheet[f'A{i}'].value)
    for i in range(2, len(positive) + len(negative) + 2):
        if sheet[f'B{i}'].value == 'да':
            Y[i - 2][0] = 1
        elif sheet[f'B{i}'].value == 'нет':
            Y[i - 2][0] = 0
    if not check:
        arguments = np.array((linalg.inv((P.transpose()).dot(P))).dot(P.transpose().dot(Y)))
    else:
        for i in range(2, len(positive) + len(negative) + 2):
            if sheet[f'B{i}'].value == 'да':
                W[i - 2][i - 2] = 1 - (func(30) - func(sheet[f'A{i}'].value))
            elif sheet[f'B{i}'].value == 'нет':
                W[i - 2][i - 2] = 1 - (math.fabs(func(0) - func(sheet[f'A{i}'].value)))
        temp = np.array(linalg.inv(((P.transpose()).dot(np.linalg.matrix_power(W, 2))).dot(P)))
        arguments = temp.dot(P.transpose().dot(np.linalg.matrix_power(W, 1)).dot(Y))
    a0 = arguments[0]
    a1 = arguments[1]


def xs(x):
    return math.exp(-x)


# логистическая функция
def func(x):
    return a0 + a1 * xs(x)
    # return (math.exp(-7 + x)) / (1 + math.exp(-7 + x))


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
