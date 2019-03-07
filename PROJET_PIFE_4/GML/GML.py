#  encoding:UTF-8
from src.medians import *
from src.file_opener import *
from src.combinaisons import *
from src.degre import *
import copy


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

"""
Paramètres :
    - marks : matrice de String
    - levels : tableau de String
    - index_level : entier
    - eleveDejaGroupe : liste d'entier
    - originalMarks : matrice de String
Résultat : retourne une liste de listes d'entiers
Méthode récursive qui permet de constituer la répartition
"""
def groupRepartition(marks, levels, index_level, eleveDejaGroupe, originalMarks):
    # On a fini, on a plus délèves disponibles
    if not(studentAvailable(marks, eleveDejaGroupe)):
        return #On fait un return vide pour indiquer qu'on a terminé.

    else:


        #Si y’a personne <= à 2 : récursivité degIn et degOut
        if(not(existsDegInOutInfOrEqual(2,marks))):
            marksUpgraded = upgrade(levels[index_level],marks)
            return groupRepartition(marksUpgraded,levels,index_level+1,eleveDejaGroupe,originalMarks)
        else:
            if(existsDegInOutInfOrEqual(0,marks)):

                return []    #Quel message pour dire qu'on a une erreur ?

            listIngoingNodesNodes = []
            # Si y’en a (sommet A) dont le degré entrant ou sortant <= 2 :
            listeSommetsInfEqTwo = getSommetsDegInOutInfEq(2, marks) #[A,B,C,D]
            listPossibleCombinations = possibleCombinations(listeSommetsInfEqTwo[0], listIngoingNodesNodes)

            tempMark = copy.deepcopy(marks)
            repartitions = []
            for group in listPossibleCombinations:
                newMarks = createGroup(group, tempMark)
                # On ajoute tous les éléments du nouveau groupe (liste) aux élèves déjà placés (liste)
                eleveDejaGroupe = eleveDejaGroupe + group

                # On reste au même niveau car il existe peut-etre d'autres sommets qui rentrent dans cette condition
                repartitions.append(groupRepartition(newMarks, levels, index_level, eleveDejaGroupe, originalMarks))

            bestRep = bestRepartition(repartitions, originalMarks)  # forme de répartitions : [ [[AB],[CD]],  [[AC], [B,D]]  ]
            return bestRep


ext = sys.argv[1][1:]
#file_preferences = open('preferences' + ext + '.csv' , 'r')  # open csv file on file_preferences
file_preferences = open('../DONNEES/preferences' + ext + '.csv' , 'r')  # open csv file on file_preferences

data_raw = file_preferences.readlines()  # data_raw va get all the values from csv file
marks = extractMarks(data_raw)
students = extractStudentsNumbers(data_raw)
marks = initialize(marks)


originalMarks = extractMarks(data_raw)
originalMarks = initialize(originalMarks)

levels = ['AR','I','P','AB','B','TB']
index_level = 0

groupsTest = groupRepartition(marks, levels, index_level, [], originalMarks)
print("La répartition est : ")
print(groupsTest)

#generateCSV(groupsTest,students)