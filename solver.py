#encoding: UTF-8
from file_opener import extractMarks, extractStudentsNumbers

def initialize(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            tab[i][j] = tab[i][j].replace('\n',"")
    return tab

# === === Methods area
def upgrade(level, marks): # enleve toutes les aretes du niveau donné en paramètre dans la matrice
    for i in range(len(marks)):
        for j in range(len(marks[i])):
            if marks[i][j] == level:
                marks[i][j] = '-1'
    return marks

def traitement(index_level, marks):
    old_marks = marks
    upgrade(levels[index_level])
    # Si un sommet inférieur ou égal à deux aretes:

    # Si le nb arete = 2 (on a un groupe de 3)
        #Soit on fait le groupe de trois
        # Soit on fait ab
        # Soit on fait ac

    # Si nb arete =1
        # On fait un groupe de 2

def formerGroupe(groupe, marks): # Supprime les sommets qui sont instanciés à partir d'une liste de numéro d'étudiant
    for eleve in groupe:  # Pour chaque élève du groupe que l'on souhaite former
        marks = supprimerSommet(eleve,marks)
    return marks

def supprimerSommet(eleve, marks): #Retourne la matrice avec le sommet rempli de -1
    for i in range(len(marks[eleve])):
        if marks[eleve][i] != '-1':
            marks[eleve][i] = '-1'

    for i in range(len(marks)):
        marks[i][eleve] = '-1'

    return marks


# === === === === === MAIN

# === === clean data from preferences

file_preferences = open('preferences.csv', 'r')  # open csv file on file_preferences
data_raw = file_preferences.readlines()  # data_raw va get all the values from csv file
marks = extractMarks(data_raw)
marks = initialize(marks)
students = extractStudentsNumbers(data_raw)
file_preferences.close()

# === === Algorithm
groups = []


levels = ['AR','I','P','AB','B','TB']
groupes = [] # Liste de tableau contenant chaque groupe: [[ABC],[BCD]]
index_level = 0

print(marks)
print("La première note est: " + str(marks[0][0]))  # First line, second column
