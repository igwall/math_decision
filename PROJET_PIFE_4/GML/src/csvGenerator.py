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

def createCSVFile(repartitions,students):
    """
       Write the CSV file
       :param repartitions: list of repartitions to write
       """
    print("\n",repartitions)
    with open('GML.csv', 'w', newline="") as csvfile:
        filewriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for rep in repartitions:
            repartition = []
            for group in rep:
                groupP = ""
                for student in group:
                    groupP = groupP + ' ' + str(students[student])
                repartition.append(groupP)
            filewriter.writerow(repartition)