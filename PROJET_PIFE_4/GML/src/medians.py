#  encoding:UTF-8

def newGroupMedian(group, marks):
    levels = ['AR','I','P','AB','B','TB']
    if(len(group)==2):
        mid = round((levels.index(marks[group[0]][group[1]])+levels.index(marks[group[1]][group[0]]))/2)
        return levels[mid]

    if(len(group)==3):
        result = ["","",""]

        result[0] = max( levels.index(marks[group[0]][group[1]]) , levels.index(marks[group[1]][group[0]]))
        result[1] = max( levels.index(marks[group[0]][group[2]]) , levels.index(marks[group[2]][group[0]]))
        result[2] = max( levels.index(marks[group[2]][group[1]]) , levels.index(marks[group[1]][group[2]]))

        result.sort()

    #we get the median (we round up if we have an even number) which corresponds to the value in the middle of our table "medians" (since it is sorted) and we retransform this value into the corresponding level
    return levels [ result[ round(len(result) / 2) ] ]


#Method which permits to return the median of the group given in parameters
#Median of groupMedians
def median(listGroup, marks):
    groupMarks = [[""] * len(listGroup) for _ in range(len(listGroup))]
    medians = []
    levels = ['AR','I','P','AB','B','TB']

    for i in listGroup:
        #groupMarks = marksGroup(i, marks)
        #medians.append(groupMedians(groupMarks)) #get medians of each relation in the group 2 by 2
        medians.append(newGroupMedian(i, marks))

    #the matrix of medians is transformed using the matrix of levels in order to be able to sort and calculate the mathematical median
    for i in range(len(medians)):
        medians[i] = levels.index(medians[i])
    medians.sort()

    #we get the median (we round up if we have an even number) which corresponds to the value in the middle of our table "medians" (since it is sorted) and we retransform this value into the corresponding level
    return levels [ medians[ round(len(medians) / 2) ] ]


#Method which returns which group of the list is the best (by using the median)
#To change : we can implement the fact that bestGroup returns more than 1 group
def bestGroup(groups, marks):
    levels = ['AR','I','P','AB','B','TB']
    medians = []

    for i in range(len(groups)):
        medians.append(levels.index(median(groups[i], marks)))

    #medians contient les indices de levels

    if (len(medians) != 0):
        maxi = max(medians) #contient l'indice max de levels

        maxValue = levels[maxi] #je recupère la valeur qui correspond à l'indice max ex : AB

        grp = []
        for i in range(len(groups)):
            grp.append(median(groups[i], marks))

        indexGroups = grp.index(maxValue)
        return groups[indexGroups]
    else:
        return []


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
