#import dependencies
import os
import collections
from collections import Counter
import csv

#define variables

totalvotes = 0
candidatevotetotal = []
voters = []
ranking = 0

#filepath
csvpath = os.path.join('Resources','election_data.csv')

#open and read file
with open(csvpath, 'r') as csvfile:
    #specify delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    #count rows and calc total number of candidates and total number of votes per candidate
    for row in csvreader:
        totalvotes = totalvotes +1
        voters.append(row[2])
    voterssort = sorted(voters)
    candidateamount = Counter (voterssort)
    candidatevotetotal.append(candidateamount.most_common())

    #calc winner and runners up
    totalrank = candidatevotetotal[0][0][1] + candidatevotetotal[0][1][1] +candidatevotetotal[0][2][1]
    gold = (candidatevotetotal[0][0][1])*100/(totalrank)     
    
    silver = (candidatevotetotal[0][1][1])*100/totalrank
    
    bronze = (candidatevotetotal[0][2][1])*100/totalrank


#print output results
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(totalvotes))
print("----------------------------")
print(str(candidatevotetotal[0][0][0]) + " " + str(gold) + "% " + str(candidatevotetotal[0][0][1]))
print(str(candidatevotetotal[0][1][0]) + " " + str(silver) + "% " + str(candidatevotetotal[0][1][1]))
print(str(candidatevotetotal[0][2][0]) + " " + str(bronze) + "% " + str(candidatevotetotal[0][2][1]))
print("Winner: " + str(candidatevotetotal[0][0][0]))
print("-------------------------")


# #create output file
election_output = os.path.join("analysis", "election_analysis.txt")
with open(election_output, "w") as output:

    output.write("Election Results\n")
    output.write("----------------------------\n")
    output.write("Total Votes: " + str(totalvotes) + "\n")
    output.write("----------------------------\n")
    output.write(str(candidatevotetotal[0][0][0]) + " " + str(gold) + "% " + str(candidatevotetotal[0][0][1]) + "\n")
    output.write(str(candidatevotetotal[0][1][0]) + " " + str(bronze) + "% " + str(candidatevotetotal[0][1][1]) + "\n")
    output.write(str(candidatevotetotal[0][2][0]) + " " + str(bronze) + "% " + str(candidatevotetotal[0][2][1]) + "\n")
    output.write("Winner: " + str(candidatevotetotal[0][0][0]) + "\n")
    output.write("----------------------------\n")