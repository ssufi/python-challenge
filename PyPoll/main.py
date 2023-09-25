import csv 
import os 

# Initialize variables to store the vote counts and candidate information
total_votes = 0
candidate_votes = {}

# Open the CSV file
INPUT_CSV_PATH = os.path.join("python-challenge","PyPoll", "election_data.csv") 
with open(INPUT_CSV_PATH) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",") 

    
    # Skip the header row
    next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        total_votes += 1  # Increment the total vote count
        
        candidate_name = row[2]  # Get the candidate's name from the third column
        
        # Check if the candidate is already in the dictionary
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1  # Increment the candidate's vote count
        else:
            candidate_votes[candidate_name] = 1  # Initialize the candidate's vote count

# Initialize variables to keep track of the winner and winning vote count
winner = ""
winning_votes = 0

# Define the path for the result file using os.path.join
result_file_path = os.path.join("python-challenge", "PyPoll", "PyPoll_Results.txt")

# Open the PyPoll_Results.txt file for writing
with open(result_file_path, "w") as resultfile:
    # Print the Election Results header to the file
    resultfile.write("Election Results\n")
    resultfile.write("-------------------------\n")
    resultfile.write(f"Total Votes: {total_votes}\n")
    resultfile.write("-------------------------\n")

    # Loop through the candidate_votes dictionary to calculate percentages and find the winner
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        resultfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        # Check if this candidate has more votes than the current winner
        if votes > winning_votes:
            winner = candidate
            winning_votes = votes

    # Print the winner to the file
    resultfile.write("-------------------------\n")
    resultfile.write(f"Winner: {winner}\n")
    resultfile.write("-------------------------\n")

print("Election results have been saved to PyPoll_Results.txt")




""" with open("PyPoll_Results.txt", "w") as resultfile:
    # Redirect standard output to the text file
    import sys
    sys.stdout = resultfile

    # Print the Election Results header
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")

    # Loop through the candidate_votes dictionary to calculate percentages and find the winner
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")
    # Check if this candidate has more votes than the current winner
        if votes > winning_votes:
            winner = candidate
            winning_votes = votes

    # Print the winner
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

# Reset standard output to the console
sys.stdout = sys.__stdout__

print("Election results have been saved to PyPoll_Results.txt") """

