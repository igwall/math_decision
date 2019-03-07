#  encoding:UTF-8
from src.medians import *
from src.file_opener import *
from src.combinaisons import *
from src.degre import *
from src.nodes import *
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
            return groupRepartition(marksUpgraded, levels, index_level+1, eleveDejaGroupe, originalMarks)
        else:
            if(existeSommetIsole(marks, eleveDejaGroupe)): # Sommet isolé et quid des gens déjà groupés

                return []    #Quel message pour dire qu'on a une erreur ?

            # Si y’en a (sommet A) dont le degré entrant ou sortant <= 2 :
            listeSommetsInfEqTwo = getSommetsDegInOutInfEq(2, marks, eleveDejaGroupe) #[A,B,C,D]
            listeLinkedNodes = linkedNodes(listeSommetsInfEqTwo[0], marks)
            listPossibleCombinations = possibleCombinations(listeSommetsInfEqTwo[0], listeLinkedNodes)

            tempMark = copy.deepcopy(marks)
            #repartitions = []
            repartitionFragment = []

            trees = []

            for group in listPossibleCombinations:
                tempMark = copy.deepcopy(marks)
                newMarks = createGroup(group, tempMark)
                groupToAdd = groupRepartition(newMarks, levels, index_level, eleveDejaGroupe+group, originalMarks)
                tree = group + groupToAdd
                trees.append(tree)

            groupe = bestRepartition(trees, originalMarks)
            return groupe



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
