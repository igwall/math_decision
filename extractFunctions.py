#encoding: UTF-8
import csv

#  Traitment function of the CSV file
#  return a list of values (marks)
def extract_marks(data_raw):

    marks = []
    for ligne in data_raw[1:]:
        ligne = ligne.split(',')[1:]
        marks.append(ligne)

    return marks
