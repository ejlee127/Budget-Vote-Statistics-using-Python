import os
import csv

#total number of months
totalmonths = 0

#net total amount of Profit/Losses
totalamount = 0

#the amount of Profit/Losses for the first month
b_amount = 0

#the amount of Profit/Losses for the row being read
c_amount = 0

#the greatest increase
g_increase = 0
gi_date = ""

#the greatest decrease
g_decrease = 0
gd_date = ""


csvfilepath = os.path.join("Resources", "budget_data.csv")
i = 0
with open(csvfilepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    #print(csvheader)

    
    for row in csvreader:

        # update values
        totalmonths += 1
        totalamount += int(row[1])
        change = int(row[1]) - c_amount
     
        #check the greatest values
        if g_increase < change:
            g_increase = change
            gi_date = row[0]

        if g_decrease > change:
            g_decrease = change
            gd_date = row[0]
        
        #keep the amount for computing change with the next amount
        c_amount = int(row[1])
        if i==0:
            b_amount = int(row[1])
        i += 1

       
    print("Total number of months = " + str(totalmonths))
    print("Total amount of the period = " + str(totalamount))
    
    avg_change = (c_amount-b_amount)/(totalmonths-1)
    
    print("Average change = " + repr(round(avg_change, 2)))
    print("The greatest increase in profits: " 
            + gi_date + " ($"+str(g_increase)+")")
    print("The greatest decrease in profits: " 
            + gd_date + " ($"+str(g_decrease)+")")