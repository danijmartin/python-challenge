import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
date_data = []
financial_data = []
profit_change = []

with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	csvheader = next(csvreader)

	#date_data = [row[0] for i in range(csvreader)]
	#financial_data = [row[1] for i in range(csvreader)]

	for row in csvreader:
		date_data.append(row[0])
		financial_data.append(int(row[1]))

# The total number of months included in the dataset
total_months = len(date_data)

print(f"Total Months: {total_months}")

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
total = sum(financial_data)

print(f"Total: ${total}")

ind_changes = [financial_data[i+1]-financial_data[i] for i in range(total_months-1)]

average_change = round((sum(ind_changes)/len(ind_changes)),2)

print(f"Average Change: ${average_change}")

# The greatest increase in profits (date and amount) over the entire period
greatest_increase = max(ind_changes)
index_greatest = ind_changes.index(greatest_increase)

greatest_month = date_data[index_greatest+1]

print(f"Greatest Increase in Profits: {greatest_month} (${greatest_increase})")

# The greatest decrease in losses (date and amount) over the entire period


#  Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)