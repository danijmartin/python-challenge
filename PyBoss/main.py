import pandas as pd

csvpath = 'Resources/employee_data.csv'

# Creating Data Frame

employee_df = pd.read_csv(csvpath)
# print(employee_df.head()) - confirming dataframe creation

# Checking data types to determine if any need to change prior to editing.
# print(employee_df.dtypes)

# Parsing Name into First Name and Last Name Columns

full_name = employee_df.Name.str.split(" ", n=1, expand=True)
employee_df['First Name'] = full_name[0]
employee_df['Last Name'] = full_name[1]
employee_df.drop(columns='Name', inplace=True)
# print(employee_df.head()) - confirming progress

# Parsing DOB to correct order
employee_df.rename(columns={'DOB': 'oldDOB'}, inplace=True)
Birthdate = employee_df.oldDOB.str.split('-', n=2, expand=True)
# print(Birthdate.head()) - confirming progress

employee_df['DOB'] = Birthdate[1] + '/' + Birthdate[2] + '/' + Birthdate[0]
employee_df.drop(columns='oldDOB', inplace=True)
# print(employee_df.head()) - confirming progress
