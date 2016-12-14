import sys
import csv
import re

REFERENCE_REGEX = r'([A-Z][0-9]+)'

def loadTableFromFile(filePath):
    table = []
    with open(filePath, 'r') as inputCSV:
        for row in csv.reader(inputCSV, delimiter=','):
            table.append(row)
    return table

def saveTableToFilePath(table, filePath):
    with open(filePath, 'w') as outputCSV:
        writer = csv.writer(outputCSV, delimiter=',')
        for row in table:
            writer.writerow(row)

# Related question:
# http://stackoverflow.com/questions/379906/parse-string-to-float-or-int
def basicTypeFromString(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s

def isBasicExpression(string):
    tokens = re.split(REFERENCE_REGEX, string[1:])[1:-1]
    return len(tokens) == 0

# Функция выдает результат вычисления выражения (формулы)
def evaluateBasicExpression(expression):
    return eval(expression)

# Функция заменяет простые строчки на простые типы int и float, если в ячейке формула без ссылок или число
def replaceBasicTypesAndExpressionsInTable(table):
    for i in range(0, len(table)):
        for j in range(0, len(table[i])):
            value = table[i][j]
            if value[0] == '=':
                if isBasicExpression(value):
                    table[i][j] = evaluateBasicExpression(value[1:])
            else:
                table[i][j] = basicTypeFromString(value)
    return table

# Функция выдает координаты ячейки по ее идентификатору (e.g. А1 = 0,0, B1 = 0,1 ...)
def tableCoordinateForLink(string):
    return (basicTypeFromString(string[1:]) - 1, ord(string[0]) - ord('A'))

# Функция превращает формулы со ссылками в обычные и считает их
def replaceReferencesInTable(table):
    pattern = re.compile(REFERENCE_REGEX)
    for i in range(0, len(table)):
        for j in range(0, len(table[i])):
            value = table[i][j]
            if isinstance(value, str):
                exp = []
                tokens = re.split(REFERENCE_REGEX, value[1:])[1:-1]
                if len(tokens) > 0 :
                    for token in tokens:
                        if pattern.match(token):  # Это ссылка
                            link = tableCoordinateForLink(token)
                            exp.append(str(table[link[0]][link[1]]))
                        else:
                            exp.append(token)
                    exp = ''.join(exp)
                    table[i][j] = evaluateBasicExpression(exp)
    return table


def computedTableFromTable(table):
    for i in range(0, len(table)):
        for j in range(0, len(table[i])):
            value = table[i][j]
            if isinstance(value, str):
                table[i][j] = evaluateBasicExpression(value[1:])
    return table

inputFilePath = sys.argv[1]
outputFilePath = sys.argv[2]
table = loadTableFromFile(inputFilePath)
table = replaceBasicTypesAndExpressionsInTable(table)
saveTableToFilePath(table, outputFilePath)
table = replaceReferencesInTable(table)