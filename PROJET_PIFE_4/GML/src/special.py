#  encoding:UTF-8
import random
import math
import sys
import csv
import copy

"""
Prends une matrice avec une seule note
"""

repartitionsPossibles = [] #variableGlobale
def specialGroupRepartition(marks):
    print("on the special repartition")
    students = []
    nbRepartitions = 10
    currentRepartition = []
    i = 0
    while i < nbRepartitions:

        while len(students) < len(marks):
            # Faire un random sur la taille du groupe (2 ou 3):
            if len(students) == len(marks) - 3 :
                size = 3
            elif len(students) == len(marks) - 2 or len(students) == len(marks) - 4:
                size = 2
            else:
                size = random.randint(2, 3)
            currentGroup = []
            while len(currentGroup) < size:
                #etudiant = math.floor( random() * len(marks)-1 )
                etudiant = random.randint(0, len(marks)-1)
                if not(etudiant in students):
                    currentGroup.append(etudiant)
                    students.append(etudiant)
            currentRepartition.append(currentGroup)

            if len(marks) >= 36:
                if len(currentRepartition) == 18:
                    repartitionsPossibles.append(currentRepartition)
                    print(currentRepartition)
                    i += 1
            else :
                repartitionsPossibles.append(currentRepartition)
                print(currentRepartition)
                i += 1


        students = []
        currentRepartition = []

    return repartitionsPossibles
