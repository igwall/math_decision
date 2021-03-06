#  encoding:UTF-8

"""
Paramètres :
    - student : int
    - marks : matrice de String
Résultat : Méthode qui permet de retourner un entier
Retourne le degré entrant d'un sommet
"""
def incomingDegree(student, marks):
    degree = 0
    columnStudent = []
    for ligne in marks:
        columnStudent.append(ligne[student])

    for i in range(0, len(columnStudent) ):
        if columnStudent[i] != '-1':
            degree = degree + 1
    return degree


"""
Paramètres :
    - student : int
    - marks : matrice de String
Résultat : Méthode qui permet de retourner un entier
Retourne le degré sortant d'un sommet
"""
def outgoingDegree(student, marks):
    degree = 0

    for i in range(0, len(marks) ):
        if marks[student][i] != '-1':
            degree = degree + 1
    return degree


"""
Paramètres :
    - degree : int
    - marks : matrice de String
Résultat : Méthode qui permet de retourner un booléen
Retourne true si il existe un noeud avec un degré entrant ou sortant == parametre
"""
def existsDegInOutInfOrEqual(degree, marks):
    existStudentWithDegInfOrEqDegree = False
    for student in range(len(marks)):
        degInInfOrEq = outgoingDegree(student,marks) <= degree
        degOutInfOrEq = incomingDegree(student,marks) <= degree
        if (degInInfOrEq or degOutInfOrEq) :
            existStudentWithDegInfOrEqDegree = True
    return existStudentWithDegInfOrEqDegree



# Retourne vrai si un sommet est isolé et pas encore placé
def existeSommetIsole(marks, eleveGroupes):
    isole = False
    for i in range(len(marks)):
        if incomingDegree(i,marks) == 0 and outgoingDegree(i,marks) == 0 not in eleveGroupes:
            isole = True
    return isole




"""
Paramètres :
    - marks : matrice de String
Résultat : Méthode qui permet de retourner un booléen
Retourne true si il existe un noeud avec un degré entrant ou sortant <= parametre
"""
#Method which returns true if it exists a node with a degree <= 2
def existsDegInOutInfOrEqual(degree, marks):
    i = 0
    found = False
    while i < len(marks) and not(found):
        if ( incomingDegree(i, marks) <= degree or outgoingDegree(i, marks) <= degree ):
            found = True
        i = i + 1
    return found


def getSommetsDegInOutInfEq(degree, marks, eleveDejaGroupe):
    studentLists = []
    for i in range(len(marks)):
        if ((incomingDegree(i,marks) <= degree) or (outgoingDegree(i,marks) <= degree)):
            if i not in eleveDejaGroupe:
                studentLists.append(i)
    return studentLists

#Methode qui retourne true si il ne reste plus qu'un seul niveau dans la matrice
def uniqueLevel(marks):
    listeNotes = [];
    nbNotesDifferentes = 0
    for student in marks:
        for elem in student:
            # Si la note est différente de -1
            if elem != '-1':
                # Si le niveau de note n'est pas dans la liste des notes déjà parcourues
                if elem not in listeNotes:
                    listeNotes.append(elem)
                    nbNotesDifferentes += 1
    print(nbNotesDifferentes == 1)
    return nbNotesDifferentes == 1
