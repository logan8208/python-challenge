import os
import csv


budg_file = os.path.join("budget_data.csv")


 


def getTotals(monthInform):

    totalMonths = 0
    netGainLoss = 0  
    avgChange = 0
    greatestInc = 0
    greatestDec = 0  
    previousVal = 0  
    totalDelta = 0

    for row in monthInform:

            totalMonths += 1

            netGainLoss += int(row[1])


            delta = (int(row[1]) - int(previousVal))

            totalDelta += delta
            
            if(delta > greatestInc):
                  greatestInc = delta

            if(delta < greatestDec):
                  greatestDec = delta

            previousVal = row[1]   

    avgChange = (totalDelta/(totalMonths-1)) 

    print()
    print("Financial Analysis")
    print("--------------------------------------------------------")    
    print(f"Total Months: {str(totalMonths)}")
    print(f"Total Gain/Loss: ${str(netGainLoss)}")
    print(f"Average  Change: ${str(avgChange)}")
    print(f"Greatest Increase in Profits: ${str(greatestInc)}")
    print(f"Greatest Decrease in Profits: ${str(greatestDec)}")



with open(budg_file, 'r') as csvfile:

      csvreader = csv.reader(csvfile, delimiter=",")

      header = next(csvreader)
      
      getTotals(csvreader)







