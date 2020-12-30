import os
import csv

#set a file path to the budget data
filePath = os.path.join("Resources","election_data.csv")

with open(filePath, 'r') as electionData:
    csvReader = csv.reader(electionData, delimiter=',')
    header = next(csvReader)
    print(header)