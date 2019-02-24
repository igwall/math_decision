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

def createGroup(group, marks): # Delete all nodes from the list of students putted in entry
    for eleve in group:  # Pour chaque élève du group que l'on souhaite former
        marks = deleteNode(eleve,marks)
    return marks

def deleteNode(eleve, marks): #Retourne la matrice avec le sommet rempli de -1
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


#Method which returns which group of the list is the best (by using the median)
def bestGroup(groups, marks):
    levels = ['AR','I','P','AB','B','TB']
    medians = []

    for i in range(len(groups)):
        medians.append( levels.index(median(groups[i], marks)) )

    maxi = max(medians)
    index = medians.index(maxi)

    return groups[index]


#Method which permits to return the incoming degree of a vertex ( = student)
def incomingDegree(student, marks):
    degree = 0
    columnStudent = []
    for ligne in marks:
        columnStudent.append(ligne[student])

    for i in range( 0, len(columnStudent) ):
        if columnStudent[i] != '-1':
            degree = degree + 1
    return degree

def minEqualTwoDegree(marks):
    i = 0
    studentDegLessEqTwo = False
    while i < len(marks) and !(studentDegLessEqTwo):
        if incomingDegree(i, marks) <= 2:
            studentDegLessEqTwo = True
        i = i + 1
    return studentDegLessEqTwo



def studentAvailable(marks):
    available = False
    for student in marks:
        for elem in student:
            if elem != '-1':
                available = True
    return available

#Method which permits to return the student with the degree given in parameters and the students linked to this student
def groups(marks, degree):
    i = 0
    students = []

    for i in range(len(marks)):
        if incomingDegree(i, marks) == degree:
            stu =[]
            stu.append(i)
            for j in range(len(marks[i])):
                if marks[i][j] != -1:
                    stu.append(j)
            students.append(stu)
        return students

# Method which try to find intersections between different groups
def intersection(listOfGroups):
    elements = []
    groupsIntersect
    for group in listOfGroups:
        for student in group:
            if student in elements:



# levels = ['AR','I','P','AB','B','TB']
def treatment(marks, levels, index_level):

    #si tous les sommets ont un degré entrant = 0 : finish return la liste des groupes
    available = studentAvailable(marks)
    if available == False:
        return []
    else:
        #supprimer les arêtes de plus bas en gardant en mémoire la matrice avant la suppression
        marksUpgraded = upgrade(index_level, marks)

        #soit personne n'a de degré entrant <= 2 -> on relance l'algo sur niveau plus haut
        if !(minEqualTwoDegree(marks)):
            return treatment(marksUpgraded, levels, index_level+1)

        #soit une personne a un degré entrant = 1 -> on crée le groupe et on relance l'algo sur niveau supérieur
        binoms = groups(marks, 1)
        if len(binoms) != 0:        # On a qu'un seul binome

        intersectedGroups = intersect(binoms) #on récupère tous les binomes en intersection
        for group in intersectedGroups:

            #Modifier en enlevant les sommets
            marksUpgraded = createGroup(binoms[0], marksUpgraded)
            return binoms[0] + treatment(marksUpgraded, levels, index_level)
        #else:         # On a plusieurs binomes et l'affectation d'un binome peut influencer un autre binome. On va descendre en profondeur.
            #Vérifier si il n'y a pas d'intersection entre les éléments qui se pointent
            #On créer les binomes sur ceux qui ne s'intersectent pas

        trinoms = groups(marks, 2)
        if len(trinoms) != 0:



        #soit une personne a un degré entrant = 2 -->
            #AB = traitment quand je fais AB
            #AC = traitment quand je fais AC
            # result = bestGroup(AB,AC) bestGroup entre le trinome et les 2 binomes possibles

        #soit une personne a un degré entrant = 0
        bitrinoms = groups(marks, 0)
        if len(bitrinoms) != 0:






# === === === === === MAIN

# === === clean data from preferences

file_preferences = open('preferences.csv', 'r')  # open csv file on file_preferences
data_raw = file_preferences.readlines()  # data_raw va get all the values from csv file
marks = extractMarks(data_raw)
marks = initialize(marks)
#qgis
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
