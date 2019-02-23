#encoding: UTF-8
import csv

#  Traitment function of the CSV file
#  return a list of values (marks) and a list of students numbers
def raw_traitment(data_raw):

    marks = []
    students_numbers = []

    for ligne in data_raw[1:]:
        ligne = ligne.split(',')[1:]
        marks.append(ligne)

    students_numbers.append(data_raw[0])

    for num in data_raw:
        students_number
    return marks, students_numbers