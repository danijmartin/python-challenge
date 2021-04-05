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
print(total_votes)

# Calculate a complete list of candidates who received votes

unique_candidates = list(set(candidates))
print(unique_candidates)

# Calculate the total number of votes each candidate won
# Calculate the percentage of votes each candidate won

c_stats = []
candidates_stats = []

for c in unique_candidates:
  c_count = candidates.count(c)
  vote_percent = round((c_count/total_votes)*100,3)
  c_stats = [c, vote_percent, c_count]
  candidates_stats.append(c_stats)

print(candidates_stats)



# Calculate the winner of the election based on popular vote.


  # Election Results
  # -------------------------
  # Total Votes: 3521001
  # -------------------------
  # Khan: 63.000% (2218231)
  # Correy: 20.000% (704200)
  # Li: 14.000% (492940)
  # O'Tooley: 3.000% (105630)
  # -------------------------
  # Winner: Khan
  # -------------------------