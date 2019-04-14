#encoding: UTF-8
import csv
import sys

#Method which permits to return a matrix of marks
"""
Parameter :
    - data_raw : list of lists
Result :
    - function which permits to extract the matrix of String composed by -1, AR, I, P, AB, B, TB
The result corresponds to the matrix of marks
"""
def extractMarks(data_raw):
    marks = []

    for ligne in data_raw[1:]:
        ligne = ligne.split(',')[1:]
        marks.append(ligne)
    return marks


"""
Parameter :
    - data_raw : list of lists
Result :
    - function which permits to extract students numbers
"""
def extractStudentsNumbers(data_raw):
    students_numbers = []
    students_numbers = csv.reader(data_raw, delimiter=',')
    result = next(students_numbers)
    final = result[1: len(result)]
    return final


def initialize(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            tab[i][j] = tab[i][j].replace('\n',"")
    return tab
