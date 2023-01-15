#import dependencies
import os
import csv

#variable definition
monthtotal = 0
currentprofitloss = 0
pastprofitloss = 0
changeloss = 0
totalprofitloss = 0
changesum = int
avgloss = float
changemax = int
changemin = int
maxmonthindex = str
minmonthindex = str
best = str
worst = str
allmonths = []
losschanges = []


#filepath
#if you're reading this, I was having trouble with my file path and had to put the full one...
#csvpath = os.path.join(r'C:\Users\kfbie\OneDrive\Desktop\python-challenge\PyBank\Resources\budget_data.csv')
csvpath = os.path.join('Resources','budget_data.csv')

#open and read file
with open(csvpath, 'r') as csvfile:
    #specify delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    
    #counting number of rows
    for row in csvreader:
        monthtotal = monthtotal +1
        #setting current profit loss
        currentprofitloss = int(row[1])
        #calculating total profit loss
        totalprofitloss = totalprofitloss + currentprofitloss
        #setting past value to current value
        if(monthtotal ==1):
            pastprofitloss = currentprofitloss
            continue
        else:
            #calculating change in loss, sum of loss, and avg loss and appending lists
            losschange = currentprofitloss - pastprofitloss
            losschanges.append(losschange)
            allmonths.append(row[0])
            pastprofitloss = currentprofitloss
            changesum = sum(losschanges)
            avgloss = (changesum/monthtotal)

    #calculating min and max loss changes alongside what months they happened in
    changemax = max(losschanges)
    changemin = min(losschanges)
    maxmonthindex = losschanges.index(changemax)
    minmonthindex = losschanges.index(changemin)

    #calculating best and worst months
    best = allmonths[maxmonthindex]
    worst = allmonths[minmonthindex]

#print results to terminal
print("Financial Analysis")
print("-----------------------------")
print("Total Months: " + str(monthtotal))
print("Total: $" + str(totalprofitloss))
print("Average Change: $" + str(avgloss))
print("Greatest Increase in Profits: " + best + str(changemax))
print("Greatest Decrease in Profits: " + worst + str(changemin))

#create output file
budget_output = os.path.join("analysis", "budget_analysis.txt")
with open(budget_output, "w") as output:

    output.write("Financial Analysis\n")
    output.write("----------------------------\n")
    output.write("Total Months: " + str(monthtotal) + "\n")
    output.write("Total: $" + str(totalprofitloss) + "\n")
    output.write("Average Change: $" + str(avgloss) + "\n")
    output.write("Greatest Increase in Profits: " + best + str(changemax) + "\n")
    output.write("Greatest Decrease in Profits: " + worst + str(changemin) + "\n")


