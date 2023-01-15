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
#if you're reading this, I was having trouble with my file path and had to put the full one...
csvpath = os.path.join(r'C:\Users\kfbie\OneDrive\Desktop\python-challenge\PyPoll\Resources\election_data.csv')

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
    print(candidatevotetotal)
    
    test = 0
    for  value in candidateamount:
        test = test+1
    print(test)

    #calc winner and runners up
    for row in candidatevotetotal:
        print(row[0][1])
        gold = (row[0][1])*100/(sum(candidateamount))     
        print(gold)
        silver = (row[1][1])*100/(sum(candidateamount))
        bronze = (row[2][1])*100/(sum(candidateamount))
    
    # total = 0
    # for value in candidateamount:
    #     total = total + value


# print("Election Results")
# print("----------------------------")
# print("Total Votes: " + totalvotes)
# print("----------------------------")
# print(str(candidatevotetotal[0][0][0]) + str(gold) + "%" + str(candidatevotetotal[0][0][1]))
# print(str(candidatevotetotal[0][0][0]) + str(silver) + "%" + str(candidatevotetotal[0][1][1]))
# print(str(candidatevotetotal[0][0][0]) + str(bronze) + "%" + str(candidatevotetotal[0][2][1]))
# print("Winner: " + str(candidatevotetotal[0][0][0]))
# print("-------------------------")


# #create output file
# election_output = os.path.join("analysis", "election_analysis.txt")
# with open(election_output, "w") as output:

#     output.write("Election Results\n")
#     output.write("----------------------------\n")
#     output.write("Total Votes: " + str(totalvotes) + "\n")
#     output.write("Total: $" + str(totalprofitloss) + "\n")
#     output.write(str(candidatevotetotal[0][0][0]) + str(gold) + "%" + str(candidatevotetotal[0][0][1]) + "\n")
#     output.write(str(candidatevotetotal[0][0][0]) + str(silver) + "%" + str(candidatevotetotal[0][1][1]) + "\n")
#     output.write("Winner: " + str(candidatevotetotal[0][0][0]) + "\n")
#     output.write("----------------------------\n")