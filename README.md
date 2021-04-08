# Python Challenge 

This repository tackles 3 problems using Python.

## PyBank

This script reviews a csv file containing two columns; month/year, and profit/loss for that month. 

The script calculates the following:
Total months in dataset
Net total of profit/loss over the entire period
Average change in profit/loss per month
Month with the greatest increase in profits and what those profits were
Month with the greatest decrease in profits and what those losses were

The script finishes by creating a csv file with the above calculations.
The output is also printed to the terminal for immediate viewing.

Output file:

#### Financial Analysis

Total Months: 86
Total: $38382578
Average Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)

## PyPoll

This script reviews voter data to determine the winner of an election.
The script reads a csv file containing three columns; Voter ID, County, and Candidate.

The following calculations are made, a csv is then created with the output and printed to the terminal:
Total votes cast
List of candidates
Total votes for each candidate and their percentage of the total votes
Winner of the election

Output file:

#### Election Results

Total Votes: 3521001

Khan: 63.0% (2218231)
Correy: 20.0% (704200)
Li: 14.0% (492940)
O'Tooley: 3.0% (105630)

Winner: Khan


## PyBoss

This challenge tackles a common issue in the business world today - cleaning data.

In this particular script, employee data is reorganized to fit a required format.

Name has been split into First Name and Last Name columns
DOB format has been changed from YYYY-MM-DD to DD/MM/YYYY
SSN has been truncated to ***-**-####
State has been abbreviated

The cleaned data is then output into a new file.