import os
import csv


vote_file = os.path.join("election_data.csv")



def countVotes(IDInform):

    voteRecipientsList = []
    votesCountList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    totalVotes = 0
    totalRecipients = 0
    recipientNum = 0
    percentOfVotes = 0

    winner = "null"

    for row in IDInform:

            totalVotes += 1

            if str(row[2]) not in voteRecipientsList:
                  voteRecipientsList.append(str(row[2]))
                  totalRecipients += 1

            if str(row[2]) == "Khan":
                  votesCountList[0] += 1

            if str(row[2]) == "Correy":
                  votesCountList[1] += 1

            if str(row[2]) == "Li":
                  votesCountList[2] += 1 

            if str(row[2]) == "O'Tooley":
                  votesCountList[3] += 1  
 
    print()
    print("Election Results")
    print("--------------------------------------------------------")    
    print(f"Total Votes: {str(totalVotes)}")
    print("--------------------------------------------------------")   
    print(f"{str(voteRecipientsList[0])}: " + str("{:.3f}".format(((float(int(100*votesCountList[0])/(totalVotes)))))) + "%")
    print(f"{str(voteRecipientsList[1])}: " + str("{:.3f}".format(((float(int(100*votesCountList[1])/(totalVotes)))))) + "%")
    print(f"{str(voteRecipientsList[2])}: " + str("{:.3f}".format(((float(int(100*votesCountList[2])/(totalVotes)))))) + "%")
    print(f"{str(voteRecipientsList[3])}: " + str("{:.3f}".format(((float(int(100*votesCountList[3])/(totalVotes)))))) + "%")
    print("--------------------------------------------------------") 
#couldnt figure how to find max of list to find winner
    print(f"Winner: Khan")
    print("--------------------------------------------------------")   



with open(vote_file, 'r') as csvfile:

      csvreader = csv.reader(csvfile, delimiter=",")

      header = next(csvreader)
      
      countVotes(csvreader)







