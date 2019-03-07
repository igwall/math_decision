"""
Parameters :
    - node : int
    - listNodes : list of int
Result :
    - list of list of int
    - Function which permits to return all the combinations of 2 possible between an int and a list of int
Example : possibleCombinationsOfTwo(1, [2,3]) = [ [1,2] , [1,3] ]
"""
def possibleCombinationsOfTwo(node, listNodes):
    combinations = []
    for i in listNodes:
        combinations.append([node,i])
    return combinations


"""
Parameters :
    - node : int
    - listNodes : list of int
Result :
    - list of list of int
    - Function which permits to return all the combinations of 3 possible between an int and a list of int
Example : possibleCombinationsOfThree(1, [2,3]) = [ [1,2,3] ]
"""
def possibleCombinationsOfThree(node, listNodes):
    combinations = []
    for j in range(0, len(listNodes)):
        k = j + 1
        for i in range(k, len(listNodes)):
            combinations.append([node,listNodes[i],listNodes[j]])
    return combinations


#  Method which permits to return all the combinations of 2 and 3 possible between a node and a list of nodes
#  example : possibleCombinationsOfThree(1, [2,3]) = [1,2], [1,3], [1,2,3]
"""
Parameters :
    - node : int
    - listNodes : list of int
Result :
    - list of list of int
    - Function which permits to return all the combinations of 2 and 3 possible between an int and a list of int
Example : possibleCombinations(1, [2,3]) = [ [1,2], [1,3], [1,2,3] ] 
"""
def possibleCombinations(node, listNodes):
    combinationsOfTwo = possibleCombinationsOfTwo(node, listNodes)
    combinationsOfThree = possibleCombinationsOfThree(node, listNodes)
    return combinationsOfTwo + combinationsOfThree
