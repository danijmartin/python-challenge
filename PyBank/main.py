import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
date_data = []
financial_data = []

with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	csvheader = next(csvreader)

	for row in csvreader:
		date_data.append(row[0])
		financial_data.append(int(row[1]))

# The total number of months included in the dataset
Total_Months = len(date_data)
print(f"Total Months: {Total_Months}")

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
total = sum(financial_data)
print(f"Total: {total}")

# The greatest increase in profits (date and amount) over the entire period


# The greatest decrease in losses (date and amount) over the entire period

#  Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)