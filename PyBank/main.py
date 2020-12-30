import os   
import csv

#set a file path to the budget data
filePath = os.path.join("Resources","budget_data.csv")

#open the budget data csv file, skip the header row
with open(filePath, 'r') as budgetFile:
    csvReader = csv.reader(budgetFile, delimiter=",")
    header = next(csvReader)

    #initialize variables
    totalMonths = 0
    netTotal = 0
    prevRowValue = 0
    netChange = 0
    maxChange = 0
    minChange = 0
    changeSum = 0

    #Get Values from first row of data (after header)
    firstRow = next(csvReader)
    totalMonths += 1
    netTotal = int(firstRow[1]) + netTotal
    prevRowValue = int(firstRow[1])

    #Count every row under the first data row to find totals
    for row in csvReader:
        totalMonths += 1
        netTotal = int(row[1]) + netTotal
        netChange = int(row[1]) - prevRowValue
        prevRowValue = int(row[1])
        changeSum = netChange + changeSum
       
        #Check the change to determine the max/min change
        if netChange > maxChange:
            maxChange = netChange
            maxChangeMonth = row[0]
        elif netChange < minChange:
            minChange = netChange
            minChangeMonth = row[0]
    
    #Calculate average of the changes (totalMonths -1, not totalMonths) 
    avgChange = round(changeSum / (totalMonths - 1),2)
    
    print(f"Financial Analysis")
    print(f"-------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${netTotal}")
    print(f"Average Change: ${avgChange}")
    print(f"Greatest Increase in Profits: {maxChangeMonth} (${maxChange})")
    print(f"Greatest Decrease in Profits: {minChangeMonth} (${minChange})")


    


