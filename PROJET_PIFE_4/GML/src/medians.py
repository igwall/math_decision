#  encoding:UTF-8
"""
Parameters :
    - listGroup : liste de int
    - marks : matrix of String
Result :
    - matrix of String
    - Method which permits to return the sub-matrix of marks of the group given in parameters
"""
def marksGroup(listGroup, marks):
    #groupMarks = []
    groupMarks = [[""] * len(listGroup) for _ in range(len(listGroup))]
    for i in range(0, len(listGroup) ):
        for j in range(0, len(listGroup) ):
            groupMarks[i][j] = marks[listGroup[i]][listGroup[j]]
    return groupMarks


"""
Parameters :
    - group : list of int
    - marks : matrix of String
Result :
    - String
    - Method which returns the minimal mark of a group
if group is empty, it returns AR
"""
def noteGroupe(group, marks):
    if len(group)!=0 and group is not None:
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


"""
Parameters :
    - repartition : list of list of int
    - marks : matrix of String
Result :
    - String
    - Method which returns the median of a repartition
"""
def medianRepartition(repartition, marks):
    if len(repartition) != 0 and repartition is not None:
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


"""
Parameters :
    - listeRepartitions :
    - marks :
Result :
"""
def bestRepartition(listeRepartitions, marks):
    if len(listeRepartitions) != 0 and listeRepartitions is not None:
        if listeRepartitions[0] is not None: #to avoid listeReparitions = [None]
            mediansRepartitions = []
            maxRepartition = []
            levels = ['AR','I','P','AB','B','TB']
            maxLevel = 0

            for repartition in listeRepartitions:
                mediansRepartitions.append(medianRepartition(repartition, marks))

            for i in mediansRepartitions:
                maxRepartition.append(levels.index(i))

            if(len(maxRepartition) == 0):
                return

            else:
                maxLevel = max(maxRepartition)
                bestLevel = levels[maxLevel]
                indexBestMedian = mediansRepartitions.index(bestLevel)

                return listeRepartitions[indexBestMedian]
