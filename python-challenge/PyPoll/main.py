import pathlib
import csv 

# Identify file location
csv_path = pathlib.Path('Resources','election_data.csv')

# Create my variables
Vote_Count = 0
Khan_Votes = 0
Correy_Votes = 0
Li_Votes = 0
Otooley_Votes = 0

# Open the csv in read mode
with open(file=csv_path, mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header labels
    csv_header = next(csvreader)
    # Loop through the rows
    for row in csvreader:
        # Calculate total votes
        Vote_Count +=1
        # Calculate total votes for each candidate
        if row[2] == "Khan":
            Khan_Votes +=1
        elif row[2] == "Correy":
            Correy_Votes +=1
        elif row[2] == "Li":
            Li_Votes +=1
        elif row[2] == "O'Tooley":
            Otooley_Votes +=1

# Calculate the percentage vote for each candidate
Khan_Percent = (Khan_Votes/Vote_Count) * 100
Correy_Percent = (Correy_Votes/Vote_Count) * 100
Li_Percent = (Li_Votes/Vote_Count)* 100
Otooley_Percent = (Otooley_Votes/Vote_Count) * 100

# Create a directory including each candidate and total votes they got
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [Khan_Votes, Correy_Votes, Li_Votes, Otooley_Votes]

# Determine which candidate got the most votes
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print the calculated values in the terminal
print("Election Results")
print("------------------")
print(f"Total Votes: {Vote_Count}")
print("------------------")
print(f"Khan: {Khan_Percent:.3f}% ({Khan_Votes})")
print(f"Correy: {Correy_Percent:.3f}% ({Correy_Votes})")
print(f"Li: {Li_Percent:.3f}% ({Li_Votes})")
print(f"O'Tooley: {Otooley_Percent:.3f}% ({Otooley_Votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

# Output a txt file to the Analysis folder
output_file = pathlib.Path("Analysis","Election_Results_Summary.txt")

# Write the txt file
with open(output_file,"w") as file:
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {Vote_Count}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Khan: {Khan_Percent:.3f}% ({Khan_Votes})")
    file.write("\n")
    file.write(f"Correy: {Correy_Percent:.3f}% ({Correy_Votes})")
    file.write("\n")
    file.write(f"Li: {Li_Percent:.3f}% ({Li_Votes})")
    file.write("\n")
    file.write(f"O'Tooley: {Otooley_Percent:.3f}% ({Otooley_Votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")