import os
import csv

csvpath = os.path.join('Resources', 'PyPoll_Resources_election_data.csv')
voter_id = []
candidates = []

with open(csvpath) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  csvheader = next(csvreader)

  for row in csvreader:
    voter_id.append(row[0])
    candidates.append(row[2])

# Calculate the total number of votes cast

total_votes = len(voter_id)

# print(total_votes)  - tested output

# Calculate a complete list of candidates who received votes

unique_candidates = list(set(candidates))

# print(unique_candidates)  - tested output

# Calculate the total number of votes each candidate won
# Calculate the percentage of votes each candidate won

candidates_stats = []

for c in unique_candidates:
  c_count = candidates.count(c)
  vote_percent = round((c_count/total_votes)*100,3)
  c_stats = [c, vote_percent, c_count]
  candidates_stats.append(c_stats)

candidates_stats.sort(key=lambda x:x[1], reverse=True )

# print(candidates_stats) - tested output

# Preparing Candidate totals for printing:

Lines = []

for lst in candidates_stats:
    line = (f'\n {lst[0]}: {lst[1]}% ({lst[2]})')
    Lines.append(line)

# print(Lines) - tested output

# Calculate the winner of the election based on popular vote.

winner = candidates_stats[0][0]

# print(winner) - tested output

# Exporting text file containing vote analysis

output_path = os.path.join('Analysis', 'Election_Results.txt')

with open(output_path, 'w') as output_file:
  output_file.write(' Election Results \n')
  output_file.write('-'*25)
  output_file.write(f'\n Total Votes: {total_votes} \n')
  output_file.write('-'*25)
  output_file.writelines(Lines)
  output_file.write('\n' + '-'*25)
  output_file.write(f'\n Winner: {winner} \n')
  output_file.write('-'*25)

# Printing final analysis to terminal

with open(output_path, 'r') as output_file:
  print(output_file.read())