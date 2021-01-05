# python-challenge
This repository contains two Python activities, PyBank and PyPoll
##PyBank
This script takes a .csv file of finanical data and creates a summary within the terminal:
- Total months of data (rows) in the file
- Total profits over the period within the file
- Average monthly change in profit within the file
- Greatest increase in profits (date and amount)
- Greatest decrease in profits (date and amount)
The script also creates a .csv file with the summary and saves it in the "Analysis" folder under the PyBank activity, with summary items as the header row and the summary item values in a single row.

##PyPoll
This scriplt takes a .csv file of election data (voter IDs, county, and selected candidate) and creates a summary within the terminal:
- Total votes counted
- All selected candidates included in the election data, including the percentage of the vote each candidate received and the total number of votes each candidate received
- The winning candidate, based on the data available in the election data file
The script also creates a .txt file which contains a copy of the summary as it is presented in the terminal