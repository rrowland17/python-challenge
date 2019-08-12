import os
import csv

poll_csv = os.path.join('Resources','election_data.csv')

def percentages(votes, total):
    return (votes / total) * 100

with open(poll_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    vote_total = 0
    candidates = []
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    Tooley_votes = 0
    Khan_percent = 0
    Correy_percent = 0
    Li_percent = 0
    Tooley_votes = 0
    vote_list = []
    
    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
        vote_total = vote_total + 1
        
        if row[2] == "Khan":
            Khan_votes += 1
        elif row[2] == "Correy":
            Correy_votes += 1
        elif row[2] == "Li":
            Li_votes += 1
        else:
            Tooley_votes += 1
         Khan_percent = percentages(Khan_votes,vote_total)
         
    Li_percent = percentages(Li_votes,vote_total)
    Correy_percent = percentages(Correy_votes,vote_total)
    Tooley_percent = percentages(Tooley_votes,vote_total)
    vote_list = [Khan_votes, Correy_votes,  Li_votes, Tooley_votes]
    winner = vote_list.index(max(vote_list))
    winner_name = candidates[winner]
    
print("Election Results")
print("-------------------------")
print(f"Total Votes: {vote_total}")
print("-------------------------")
print(f"Khan: {Khan_percent:.03f}% ({Khan_votes})")
print(f"Correy: {Correy_percent:.03f}% ({Correy_votes})")
print(f"Li: {Li_percent:.03f}% ({Li_votes})")
print(f"O'Tooley: {Tooley_percent:.03f}% ({Tooley_votes})")
print("-------------------------")
print(f"Winner: {winner_name}")
print("-------------------------")

output = os.path.join("PollSummary.txt")

with open (output,"w") as new:
    new.write("Election Results")
    new.write("\n")
    new.write("-------------------------")
    new.write("\n")
    new.write(f"Total Votes: {vote_total}")
    new.write("\n")
    new.write("-------------------------")
    new.write("\n")
    new.write(f"Khan: {Khan_percent:.03f}% ({Khan_votes})")
    new.write("\n")
    new.write(f"Correy: {Correy_percent:.03f}% ({Correy_votes})")
    new.write("\n")
    new.write(f"Li: {Li_percent:.03f}% ({Li_votes})")
    new.write("\n")
    new.write(f"O'Tooley: {Tooley_percent:.03f}% ({Tooley_votes})")
    new.write("-------------------------")
    new.write("\n")
    new.write(f"Winner: {winner_name}")
    new.write("\n")
    new.write("-------------------------")
            
