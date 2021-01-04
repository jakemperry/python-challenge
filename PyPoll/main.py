import os
import csv

#set a file path to the budget data
filePath = os.path.join("Resources","election_data.csv")

with open(filePath, 'r') as electionData:
    csvReader = csv.reader(electionData, delimiter=',')
    header = next(csvReader)
    print(header)

    #Create an empty set for candidates (based on example from class materials)
    allCandidates=set()
    totalVotes = 0
    winnerName = "N/A"
    mostVotes = 0

    #read all rows and fill out set of unique candidates
    for row in csvReader:
        allCandidates.add(row[2])
        totalVotes += 1
    print(allCandidates)
#Create a dictionary with the candidates set as the keys, initial values = 0 (based on example from class materials)
voteCount={}.fromkeys(allCandidates,0)

#Open the csv file again
with open(filePath, 'r') as electionData:
    csvReader = csv.reader(electionData, delimiter=',')
    header = next(csvReader)
    #Go through each row, add to the count for every candidate (based on example from class materials)
    for row in csvReader:
        voteCount[row[2]] += 1
    #Find the candidate with the most votes after counting all votes for all candidates    
    for candidate, count in voteCount.items():
        if count > mostVotes:
            mostVotes = count
            winnerName = candidate
    
#Print Results
print(f"Election Results")
print(f"--------------------------")
print(f"Total Votes: {totalVotes}")
print(f"--------------------------")
for candidate, count in voteCount.items():
    print(f"{candidate}: {round((count/totalVotes)*100,3)}% ({count})")
print(f"--------------------------")
print(f"Winner: {winnerName}")
print(f"--------------------------")