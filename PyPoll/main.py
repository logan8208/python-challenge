import os
import csv


vote_file = os.path.join("election_data.csv")



def countVotes(IDInform):

    voteRecipients = []

    totalVotes = 0
    totalRecipients = 0
    recipientNum = 0
    percentOfVotes = 0

    winner = "null"


    for row in IDInform:

            totalVotes += 1

            if str(row[2]) not in voteRecipients:
                  voteRecipients.append(str(row[2]))
                  totalRecipients += 1
                  recipientNum = 0
            

            
                  
    print()
    print(f"The following people received votes: {voteRecipients}")


    print()
    print("Election Results")
    print("--------------------------------------------------------")    
    print(f"Total Votes: {str(totalVotes)}")
    print("--------------------------------------------------------")   




    print("--------------------------------------------------------") 
    print(f"Winner: {str(winner)}")
    print("--------------------------------------------------------")   



with open(vote_file, 'r') as csvfile:

      csvreader = csv.reader(csvfile, delimiter=",")

      header = next(csvreader)
      
      countVotes(csvreader)







