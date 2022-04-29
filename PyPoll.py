# Add our dependencies
import os
import csv

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0
county_total_votes = 0

# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list = []
county_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    # For each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        county_total_votes +=1
        # Print the candidate name from each row
        candidate_name = row[2]
        # 3: Extract the county name from each row.
        county_name = row[1]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name]=0
        # Add a vote to that candidate's name
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:
            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)
            # 4c: Begin tracking the county's vote count.
            county_votes[county_name]=0
            # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n"
        f"County Votes:\n")
    print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        countyvotes = county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county.
        county_percentage = float(countyvotes) / float(county_total_votes) * 100
        # 6d: Print the county results to the terminal.
        county_results = (f'{county_name}: {county_percentage:.1f}% ({countyvotes:,})\n')
        print(county_results)
        # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

        # 6f: Write an if statement to determine the winning county and get its vote count.
        if (countyvotes > winning_county_count) and (county_percentage > winning_county_percentage):
            winning_county_count = countyvotes
            winning_county_percentage = county_percentage
            winning_county = county_name

    # 7: Print the county with the largest turnout to the terminal.
    winning_county_summary = (
        f'-----------------------\n'
        f'Largest County Turnout: {winning_county}\n'
        f'-----------------------\n')
    print(winning_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)

    # Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
        # Print each candidate's voter count and percentage
        print(candidate_results)
        # Save the candidate results to the text file
        txt_file.write(candidate_results)
        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

    # Print winning candidate summary
    winning_candidate_summary = (
        f'--------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'---------------------------\n')
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)




