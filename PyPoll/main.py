#import my dependencies
import os
import csv


#define all variables
total_votes = 0
votes_for_khan = 0
votes_for_correy = 0
votes_for_li = 0
votes_for_otooley = 0

#create a file path for the data
election_data_path = os.path.join("../PyPoll/Resources/election_data.csv")


#open and read the data path
with open(election_data_path) as election_data_file:
    reader = csv.reader(election_data_file, delimiter=',')

    #read the header first
    header = next(election_data_file)


    #read the row of data after the header
    for row in reader:


        #calculate the total number of votes cast
        total_votes += 1


        #calculate the total number of votes per candidate
        if(row[2] == "Khan"):
            votes_for_khan += 1
        elif (row[2] == "Correy"):
            votes_for_correy += 1
        elif (row[2] == "Li"):
            votes_for_li += 1
        else:
            votes_for_otooley += 1


    #calculate the percentage of votes won per candidate
    percent_khan = votes_for_khan / total_votes
    percent_correy = votes_for_correy / total_votes
    percent_li = votes_for_li / total_votes
    percent_otooley = votes_for_otooley / total_votes


    #calculate the winner of the election via popular votes
    popular_winner = max(votes_for_khan, votes_for_correy, votes_for_li, votes_for_otooley)


    if popular_winner == votes_for_khan:
        name_of_winner = "Khan"
    elif popular_winner == votes_for_correy:
        name_of_winner = "Correy"
    elif popular_winner == votes_for_li:
        name_of_winner = "Li"
    else:
        name_of_winner = "O'Tooley"

#print the analysis
print(f"Election Results")
print(f"--------------------------")
print(f"Total Votes: {total_votes}")
print(f"--------------------------")
print(f"Kahn: {percent_khan:.3%} ({votes_for_khan})")
print(f"Correy: {percent_correy:.3%} ({votes_for_correy})")
print(f"Li: {percent_li:.3%} ({votes_for_li})")
print(f"O'Tooley: {percent_otooley:.3%} ({votes_for_otooley})")
print(f"---------------------------")
print(f"The Winner Is: {name_of_winner}")
print(f"---------------------------")


#delegating what file to write edited data to
result_voter_file = os.path.join("../PyPoll/Analysis/election_data_revised.txt")


#open the file as a text file
with open(result_voter_file, 'w',) as txtfile:


    #write the data in new format
    txtfile.write(f"Election Results\n")
    txtfile.write(f"--------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"--------------------------\n")
    txtfile.write(f"Kahn: {percent_khan:.3%} ({votes_for_khan})\n")
    txtfile.write(f"Correy: {percent_correy:.3%} ({votes_for_correy})\n")
    txtfile.write(f"Li: {percent_li:.3%} ({votes_for_li})\n")
    txtfile.write(f"O'Tooley: {percent_otooley:.3%} ({votes_for_otooley})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"The Winner Is: {name_of_winner}\n")
    txtfile.write(f"---------------------------\n")
