def listIngoingNodes(student, marks):
    ingoingNodes = []
    for i in range(len(marks)):
        if marks[i][student] != '-1':
            ingoingNodes.append(i)
    return ingoingNodes


def listOutgoingNodes(student, marks):
    outgoingNodes = []
    for i in range(len(marks)):
        if marks[student][i] != '-1':
            outgoingNodes.append(i)
    return outgoingNodes


def linkedNodes(student, marks):
    return listIngoingNodes(student, marks) + listOutgoingNodes(student, marks)
