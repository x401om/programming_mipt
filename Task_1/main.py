import sys
import csv
import re
from math import *

REFERENCE_REGEX = r'(\w\d+)'

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

def cutoffDecimalsIfNeeded(value):
    if isinstance(value, float):
        return float(str('{0:.5f}'.format(value)))
    else:
        return value

def wrapStringToQuotesIfNeeded(value):
    if isinstance(value, str):
        value = basicTypeFromString(value)
        if isinstance(value, str):
            value = '"{0}"'.format(value)
        else:
            value = str(value)
    return value

def isBasicExpression(string):
    tokens = re.split(REFERENCE_REGEX, string[1:])[1:-1]
    return len(tokens) == 0

# This function evaluates the expression (function)
def evaluateBasicExpression(expression):
    return eval(expression)

# Replaces basic strings with basic types as int or float
# if there is basic fromula without references or number
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

# Calculates the coordinates of cell from its id
def tableCoordinateForLink(string):
    return (basicTypeFromString(string[1:]) - 1, ord(string[0]) - ord('A'))

# Converts formulas with references to basics and calculates them
def replaceReferencesInTable(table):
    pattern = re.compile(REFERENCE_REGEX)
    for i in range(0, len(table)):
        for j in range(0, len(table[i])):
            value = table[i][j]
            if isinstance(value, str):
                tokens = re.split(REFERENCE_REGEX, value[1:])[1:-1]
                if len(tokens) > 0:
                    for token in tokens:
                        if pattern.match(token):  # This is a link
                            link = tableCoordinateForLink(token)
                            referenceValue = str(table[link[0]][link[1]])
                            referenceValue = wrapStringToQuotesIfNeeded(referenceValue)
                            value = value.replace(token, referenceValue)
                    value = evaluateBasicExpression(value[1:])
                    table[i][j] = cutoffDecimalsIfNeeded(value)
    return table

inputFilePath = sys.argv[1]
outputFilePath = sys.argv[2]

if len(sys.argv) > 3:
    extraFunctionsFilePath = sys.argv[3]
    with open(extraFunctionsFilePath, 'r') as functions:
        exec(functions.read())

table = loadTableFromFile(inputFilePath)
table = replaceBasicTypesAndExpressionsInTable(table)
table = replaceReferencesInTable(table)
saveTableToFilePath(table, outputFilePath)
