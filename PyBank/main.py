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

total_months = len(date_data)

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

total = sum(financial_data)

ind_changes = [financial_data[i+1]-financial_data[i] for i in range(total_months-1)]

average_change = round((sum(ind_changes)/len(ind_changes)),2)

# The greatest increase in profits (date and amount) over the entire period

greatest_increase = max(ind_changes)

index_greatest = ind_changes.index(greatest_increase)

greatest_month = date_data[index_greatest+1]

# The greatest decrease in losses (date and amount) over the entire period

greatest_decrease = min(ind_changes)

index_least = ind_changes.index(greatest_decrease)

least_month = date_data[index_least+1]

# Final Analysis

months = (f"\nTotal Months: {total_months} \n")
profit = (f"Total: ${total} \n")
profit_change = (f"Average Change: ${average_change} \n")
profit_increase = (f"Greatest Increase in Profits: {greatest_month} (${greatest_increase}) \n")
profit_decrease = (f"Greatest Decrease in Profits: {least_month} (${greatest_decrease}) \n")
Lines = [months, profit, profit_change, profit_increase, profit_decrease]

# Exporting text file containing final analysis

output_path = os.path.join('Analysis', 'Financial_Analysis.txt')

with open(output_path, 'w') as output_file:
	output_file.write('Financial Analysis \n')
	output_file.write('-'*25)
	output_file.writelines(Lines)

# Printing final analysis to terminal

with open(output_path, 'r') as output_file:
	print(output_file.read())
