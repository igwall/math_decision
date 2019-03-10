def listIngoingNodes(student, marks):
    ingoingNodes = []
    for i in range(len(marks)):
        if marks[i][student] != '-1':
            ingoingNodes.append(i)
    return ingoingNodes


def listOutgoingNodes(student, marks):
    outgoingNodes = []
    for i in range(len(marks)):
        if marks[student][i] != '-1':
            outgoingNodes.append(i)
    return outgoingNodes


def linkedNodes(student, marks):
    return listIngoingNodes(student, marks) + listOutgoingNodes(student, marks)

def studentAvailable(marks, eleveDejaGroupe):
    available = False
    if(len(eleveDejaGroupe)!=len(marks[0])):
        available = True
    return available

def createGroup(group, marks): # Delete all nodes from the list of students putted in entry
    print("on cree le groupe : ", group)
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

def upgrade(level, marks):  # enleve toutes les aretes du niveau donné en paramètre dans la matrice
    for i in range(len(marks)):
        for j in range(len(marks[i])):
            if marks[i][j] == level:
                marks[i][j] = '-1'
    return marks
