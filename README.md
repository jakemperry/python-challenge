<h1>python-challenge</h1>
This repository contains two Python activities, PyBank and PyPoll

<h2>PyBank</h2>
This script takes a .csv file of finanical data and creates a summary within the terminal:
<ul>
    <li>Total months of data (rows) in the file</li>
    <li>Total profits over the period within the file</li>
    <li>Average monthly change in profit within the file</li>
    <li>Greatest increase in profits (date and amount)</li>
<li>Greatest decrease in profits (date and amount)</li>
</ul>
The script also creates a .csv file with the summary and saves it in the "Analysis" folder under the PyBank activity, with summary items as the header row and the summary item values in a single row.

<h2>PyPoll</h2>
This scriplt takes a .csv file of election data (voter IDs, county, and selected candidate) and creates a summary within the terminal:
<ul>
    <li>Total votes counted</li>
    <li>All selected candidates included in the election data, including the percentage of the vote each candidate received and the total number of votes each candidate received</li>
    <li>The winning candidate, based on the data available in the election data file</li>
</ul>
The script also creates a .txt file which contains a copy of the summary as it is presented in the terminal, this file is saved in the "Analysis" folder (if no such folder already exists, the script will create an "Analysis" folder)