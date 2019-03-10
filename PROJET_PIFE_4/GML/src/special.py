#  encoding:UTF-8
from src.medians import *
from file_opener import *
from src.combinaisons import *
from src.degre import *
from src.nodes import *
from src.csvGenerator import *
import copy



"""
Prends une matrice avec une seule note
"""
repartitionsPossibles = [] #variableGlobale
def specialGroupRepartition(marks, levels, index_level, eleveDejaGroupe, originalMarks, repartitionEnCours):
    if len(repartitionsPossibles) >= 20 :
        bestRep = bestRepartition(repartitionsPossibles, originalMarks)
        print(bestRep)
        print(medianRepartition(bestRep, originalMarks))
        sys.exit()

    if not(studentAvailable(marks, eleveDejaGroupe)):
        print("finish")
        repartitionsPossibles.append( repartitionEnCours )
        return #On fait un return vide pour indiquer qu'on a terminé.



    #Une combinaison, puis relancer l'algo sur tout le reste sans la combinaison faite
    else:
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

                groupToAdd = specialGroupRepartition(newMarks, levels, index_level, tempEleveDejaGroupe, originalMarks, tempRepEnCours)
