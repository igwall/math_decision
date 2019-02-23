#encoding: UTF-8
from file_opener import raw_traitment


# === === clean data from preferences

file_preferences = open('preferences.csv', 'r')  # open csv file on file_preferences
data_raw = file_preferences.readlines()  # data_raw va get all the values from csv file
marks, students = raw_traitment(data_raw)


# === ===

#print("Le premier élève est: " + str(students[0]))
print("Liste des élèves: " + str(students))
print("La première note est: " + str(marks[0][1]))  # First line, second column