
import csv

csvpath = "Resources/election_data.csv"

# This will import data from the csv file.
# It will set up lists for candidate and candidatelist.  
# It will then calculate votes by candidate and add that to a dictionary - votes
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter = ',')
    csv_header = next(csvreader)


    Candidate = []
    CandidateList = []
    TotalVoters = 0
    votes = {}
  #  CandidateDict = {}


    for row in csvreader:
        Candidate = row[2]
        if Candidate not in CandidateList:
            CandidateList.append(Candidate)
            votes[Candidate] = 0
        votes[Candidate] +=1
        TotalVoters += 1


#We will now print out the results.  In the midst of printing this out, we'll calculate the % of votes cast
# for each candidate, and we will also declare a winner based on the highest number of votes.

    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str('{:,.0f}'.format(TotalVoters)))
    print("-------------------------")
    for i in votes:
        PctVotes = '{:,.3f}'.format((votes[i]/TotalVoters)*100)
        print(i + ": "+ str(PctVotes) + "% (" + str('{:,.0f}'.format(votes[i])) + ")")
    print("-------------------------")
    keyMax = max(votes, key=votes.get)
    print("Winner:  " + keyMax)
    print("-------------------------")


#Now we'll make an output file with the same information printed out to the terminal.  this will be found in 
# the file py_Poll_Results.txt

#output="py_Poll_Results.txt"
#with open(output,"w+") as file:
#    file.write("Election Results\n")
#    file.write("-------------------------\n")
#    file.write("Total Votes: " + str('{:,.0f}'.format(TotalVoters)) + "\n")
#    file.write("-------------------------\n")
#    for i in votes:
#        PctVotes = '{:,.3f}'.format((votes[i]/TotalVoters)*100)
#        file.write(i + ": "+ str(PctVotes) + "% (" + str('{:,.0f}'.format(votes[i])) + ")\n")
#    file.write("-------------------------\n")
#    keyMax = max(votes, key=votes.get)
#    file.write("Winner:  " + keyMax + "\n")
#    file.write("-------------------------\n")
