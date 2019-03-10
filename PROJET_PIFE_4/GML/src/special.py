#  encoding:UTF-8
from medians import *
from file_opener import *
from combinaisons import *
from degre import *
from nodes import *
from csvGenerator import *
import copy

repartitionsPossibles = [] #variableGlobale
def groupRepartition(marks, levels, index_level, eleveDejaGroupe, originalMarks, repartitionEnCours):
    if len(repartitionsPossibles) >= 100 :
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




def specialGroupRepartition(marks, levels, index_level, eleveDejaGroupe, originalMarks, repartitionEnCours):


    if existeSommetIsole(marks, eleveDejaGroupe):

        #  Il n'y a pas de sommet isolé
        else:
