import os   
import csv

#set a file path to the budget data
filePath = os.path.join("Resources","budget_data.csv")

#open the budget data csv file, skip the header row
with open(filePath, 'r') as budgetFile:
    csvReader = csv.reader(budgetFile, delimiter=",")
    header = next(csvReader)

    #initialize the monthCount variable
    monthCount = 0

    #Count every row under the header to find total months
    for row in csvReader:
        monthCount += 1
    
    print(monthCount)


