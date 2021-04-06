import pandas as pd
import re

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

# Truncating SSN

employee_df.SSN = employee_df.SSN.apply(lambda x: re.sub(r'\d', '*', x, count=5))
# print(employee_df.head()) - confirming progress

# Abbreviating States

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands': 'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'Washington DC': 'DC',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

employee_df.State.replace(us_state_abbrev, inplace=True)
# print(employee_df.head())  - confirming progress

# Returning columns to original order

employee_df = employee_df[['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']]
# print(employee_df.head())  - confirming progress

# Rewriting file for future use

employee_df.to_csv('Resources/clean_employee_data.csv')