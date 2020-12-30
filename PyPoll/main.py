import os
import csv

#set a file path to the budget data
filePath = os.path.join("Resources","election_data.csv")

with open(filePath, 'r') as electionData:
    csvReader = csv.reader(electionData, delimiter=',')
    header = next(csvReader)
    print(header)

    #Create an empty set for candidates
    allCandidates=set()
    totalVotes = 0

    #read all rows and fill out set of unique candidates
    for row in csvReader:
        allCandidates.add(row[2])
        totalVotes += 1
    print(allCandidates)
#Create a dictionary with the candidates set as the keys, initial values = 0
voteCount={}.fromkeys(allCandidates,0)

#Open the csv file again
with open(filePath, 'r') as electionData:
    csvReader = csv.reader(electionData, delimiter=',')
    header = next(csvReader)
    #Go through each row, add to the count for every candidate
    for row in csvReader:
        voteCount[row[2]] += 1
print(voteCount)