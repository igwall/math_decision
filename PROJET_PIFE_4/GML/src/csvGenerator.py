#encoding:UTF-8
import csv
def generateCSV(repartition,students):
    listStudent= []
    print(students)
    for group in repartition:
        actualGroup = []
        print(group)
        for index in group:
            print(students[index])
            actualGroup.append(students[index])
        print(actualGroup)
        listStudent.append(actualGroup)
    createCSVFile(listStudent)

def createCSVFile(repartition):
    with open('GML.csv', 'w', newline="") as csvfile:
        filewriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for group in repartition:
            groupP = ""
            for student in group:
                groupP = groupP + ' ' + str(student)
            repartition.append(groupP)
            filewriter.writerow(repartition)
