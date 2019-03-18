#  encoding:UTF-8
from src.medians import *
from src.file_opener import *
from src.combinaisons import *
from src.degre import *
from src.nodes import *
from src.csvGenerator import *
from src.special import *
import copy

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
    if len(repartitionsPossibles) >= 10000 :
        bestRep = bestRepartition(repartitionsPossibles, originalMarks)
        print(bestRep)
        print(medianRepartition(bestRep, originalMarks))
        sys.exit()

    # On a fini, on a plus délèves disponible et tous le monde a été placé
    if not(studentAvailable(marks, eleveDejaGroupe)) and len(eleveDejaGroupe) == len(marks):
        print("finish")
        repartitionsPossibles.append( repartitionEnCours )
        return #On fait un return vide pour indiquer qu'on a terminé.

    else:
        #Si y’a personne <= à 2 : récursivité degIn et degOut mais qu'on est pas au niveau de TB
        if(not(existsDegInOutInfOrEqual(2,marks)) and not(uniqueLevel(marks))):
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
groupsTest = []
if uniqueLevel(marks):
    groupsTest = specialGroupRepartition(marks)
else:
    groupsTest = groupRepartition(marks, levels, index_level, [], originalMarks, [])

print("La répartition est : ")
#print(groupsTest)
print(repartitionsPossibles)
print(len(repartitionsPossibles))
createCSVFile(repartitionsPossibles,students)
