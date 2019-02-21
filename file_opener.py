import csv

f1 = open("preferences.csv","r")
lignes = f1.readlines()

for ligne in lignes[1:]:
  ligne = ligne.split(',')[1:]
  print(ligne)

f1.close()



#  Traitment function of the CSV file
#  return a list of values (marks) and a list of students numbers
def raw_traitment(data_raw):
    next(data_raw)  # skip header
    student_numbers = []
    marks = []

    lignes = data_raw.readlines()
    for ligne in lignes[1:]:
        ligne = ligne.split(',')[1:]
        marks.append(ligne)


        # TODO: Retirer l'ensemble des numéros étudiants sur la ligne


    return marks, student_numbers


# Main

print("Ouverture du fichier de préférences")


file_preferences = open('preferences.csv', 'r')  # open csv file on file_preferences

data_raw = csv.reader(file_preferences)  # data_raw va get all the values from csv file

mark, students = raw_traitment(data_raw)  # Send the data to the traitment function to clean them.

print("La premiere note est: " + mark[0][0])
