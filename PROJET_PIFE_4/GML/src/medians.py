#  encoding:UTF-8
"""
Parameters :
    - listGroup :
    - marks :
Résultat Method which permits to return the sub-matrix of marks of the group given in parameters
"""
def marksGroup(listGroup, marks):
    #groupMarks = []
    groupMarks = [[""] * len(listGroup) for _ in range(len(listGroup))]
    for i in range(0, len(listGroup) ):
        for j in range(0, len(listGroup) ):
            groupMarks[i][j] = marks[listGroup[i]][listGroup[j]]
    return groupMarks


"""
Paramètres :
    - group : liste d'entiers
    - marks : matrice de String
Résultat : permet de retourner la note min d'un groupe
"""
def noteGroupe(group, marks):
    levels = ['AR','I','P','AB','B','TB']
    groupMarks = []
    groupMarks = marksGroup(group, marks)

    notes = []
    minNote = 0

    for i in range(0, len(groupMarks) ):
        for j in range(0, len(groupMarks) ):
            if i != j :
                notes.append(levels.index(groupMarks[i][j]))

    minNote = min(notes)
    return levels[minNote]



def medianRepartition(repartition, marks):
    levels = ['AR','I','P','AB','B','TB']
    notes = []
    medians = []

    for group in repartition :
        notes.append(noteGroupe(group,marks))

    for i in range(len(notes)):
        medians.append( levels.index(notes[i]) )
    medians.sort()

    #le ifelse à cause du décalage du aux indices qui commencent à zéro
    if len(medians)/2 == round( len(medians) / 2 ):
        return levels[medians[round( len(medians) / 2)]]
    else:
        return levels[medians[round( (len(medians) - 1) / 2)]]



def bestRepartition(listeRepartitions, marks):
    mediansRepartitions = []
    maxRepartition = []
    levels = ['AR','I','P','AB','B','TB']
    maxLevel = 0

    for repartition in listeRepartitions:
        mediansRepartitions.append(medianRepartition(repartition, marks))

    for i in mediansRepartitions:
        maxRepartition.append(levels.index(i))

    maxLevel = max(maxRepartition)
    bestLevel = levels[maxLevel]
    indexBestMedian = mediansRepartitions.index(bestLevel)

    return listeRepartitions[indexBestMedian]

