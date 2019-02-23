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



#Method which permits to return the sub-matrix of marks of the group given in parameters
def marksGroup(listGroup, marks):
    groupMarks = [[""] * len(listGroup) for _ in range(len(listGroup))]
    for i in range(0, len(listGroup) ):
        for j in range(0, len(listGroup) ):
            groupMarks[i][j] = marks[ listGroup[i] ][ listGroup[j] ]
    return groupMarks


#Methods which permits to return medians 2 by 2 of a group of students
def groupMedians(groupMarks):
    medians = []
    levels = ['AR','I','P','AB','B','TB']
    for i in range(len(groupMarks)):
        for j in range(len(groupMarks[i])):
            if i != j: #condition to eliminate the "-1" value

                #as we have 2 values (mark of the student A on B and reciprocally) , the median is the largest
                #we use the table level to do the correspondence
                if levels.index(groupMarks[i][j]) > levels.index(groupMarks[j][i]):
                    median = groupMarks[i][j]
                else:
                    median = groupMarks[j][i]

                medians.append(median)
    return medians


#Method which permits to return the median of the group given in parameters
def median(listGroup, marks):
    groupMarks = [[""] * len(listGroup) for _ in range(len(listGroup))]
    medians = []
    levels = ['AR','I','P','AB','B','TB']

    groupMarks = marksGroup(listGroup, marks)

    medians = groupMedians(groupMarks) #get medians of each relation in the group 2 by 2

    #the matrix of medians is transformed using the matrix of levels in order to be able to sort and calculate the mathematical median
    for i in range(len(medians)):
        medians[i] = levels.index(medians[i])
    medians.sort()

    #we get the median (we round up if we have an even number) which corresponds to the value in the middle of our table "medians" (since it is sorted) and we retransform this value into the corresponding level
    return levels [ medians[ round(len(medians) / 2) ] ]


#Method which returns which group of the 2 is the best (by using the median)
def bestGroup(listGroup1, listGroup2, marks):
    levels = ['AR','I','P','AB','B','TB']

    medianValue1 = levels.index( median(listGroup1, marks) )
    medianValue2 = levels.index( median(listGroup2, marks) )
    if (medianValue1 > medianValue2):
        return listGroup1
    else:
        return listGroup2



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

print(median([5, 4 ,6], marks))

print(bestGroup([4,5,6], [2,6,8], marks))
print(bestGroup([0,1,2], [0,39,9], marks))
print(bestGroup([0,9,39], [1,4,5], marks))
