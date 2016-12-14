import sys
import csv

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
        return float(s)

# Функция заменяет простые строчки на простые типы int и float, если в ячейке не формула
def replaceBasicTypesInTable(table):
    for i in range(0, len(table)):
        for j in range(0, len(table[i])):
            value = table[i][j]
            if value[0] != '=':
                table[i][j] = basicTypeFromString(value)
    return table

# Функция выдает результат вычисления выражения (формулы)
def evaluateBasicExpression(expression):
    return eval(expression)

# Функция просчитывает значения для всех ячеек
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
table = replaceBasicTypesInTable(table)
table = computedTableFromTable(table)
saveTableToFilePath(table, outputFilePath)