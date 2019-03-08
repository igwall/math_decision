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
    - repartitionEnCours : liste de int
Résultat : retourne une liste de listes d'entiers
Méthode récursive qui permet de constituer la répartition
"""
repartitionsPossibles = [] #variableGlobale
def groupRepartition(marks, levels, index_level, eleveDejaGroupe, originalMarks, repartitionEnCours):
    if len(repartitionsPossibles) >= 1000 :
        bestRep = bestRepartition(repartitionsPossibles, originalMarks)
        print(bestRep)
        print(medianRepartition(bestRep, originalMarks))
        sys.exit()
    # On a fini, on a plus délèves disponible
    if not(studentAvailable(marks, eleveDejaGroupe)):
        print("finish")
        repartitionsPossibles.append( repartitionEnCours )
        return #On fait un return vide pour indiquer qu'on a terminé.
    else:
        #Si y’a personne <= à 2 : récursivité degIn et degOut
        if(not(existsDegInOutInfOrEqual(2,marks))):
            marksUpgraded = upgrade(levels[index_level],marks)
            return groupRepartition(marksUpgraded, levels, index_level+1, eleveDejaGroupe, originalMarks, repartitionEnCours)
        else:
            if(existeSommetIsole(marks, eleveDejaGroupe)): # Sommet isolé et quid des gens déjà groupés
                return []    #Quel message pour dire qu'on a une erreur ?

            # Si y’en a (sommet A) dont le degré entrant ou sortant <= 2 :
            listeSommetsInfEqTwo = getSommetsDegInOutInfEq(2, marks, eleveDejaGroupe) #[A,B,C,D]
            if( len(listeSommetsInfEqTwo) != 0 ):
                listeLinkedNodes = linkedNodes(listeSommetsInfEqTwo[0], marks)
                listPossibleCombinations = possibleCombinations(listeSommetsInfEqTwo[0], listeLinkedNodes)
                tempMark = copy.deepcopy(marks)

                for group in listPossibleCombinations:
                    print("group", group)
                    tempMark = copy.deepcopy(marks)
                    newMarks = createGroup(group, tempMark)

                    #sinon on utilise la liste du tour d'avant
                    tempEleveDejaGroupe = copy.deepcopy(eleveDejaGroupe)
                    tempEleveDejaGroupe = eleveDejaGroupe + group

                    tempRepEnCours = copy.deepcopy(repartitionEnCours)
                    tempRepEnCours.append( group )

                    groupToAdd = groupRepartition(newMarks, levels, index_level, tempEleveDejaGroupe, originalMarks, tempRepEnCours)



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

groupsTest = groupRepartition(marks, levels, index_level, [], originalMarks, [])
print("La répartition est : ")
#print(groupsTest)
print(repartitionsPossibles)
#generateCSV(groupsTest,students)
