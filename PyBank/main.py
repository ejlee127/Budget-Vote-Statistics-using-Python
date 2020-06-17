import os
import csv

#set the input file path
csvfilepath = os.path.join("Resources", "budget_data.csv")

#the greatest increase and its date
g_increase = 0
gi_date = ""
    
#the greatest decrease and its date
g_decrease = 0
gd_date = ""

#open the input file
with open(csvfilepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    #print(csvheader)
    
    #Read the first row and initialnize the values
    firstrow = next(csvreader)

    #the amount of Profit/Losses for the first month
    first_amount = int(firstrow[1])

    #total number of months
    total_months = 1

    #net total amount of Profit/Losses
    total_amount = first_amount
    
    #the amount of Profit/Losses for the previous month
    prev_amount = first_amount

    for row in csvreader:

        # update values
        date = row[0]
        new_amount = int(row[1])
        total_months += 1
        total_amount += new_amount
        change = new_amount - prev_amount
     
        #check the greatest values
        if g_increase < change:
            g_increase = change
            gi_date = date

        if g_decrease > change:
            g_decrease = change
            gd_date = date
        
        #Update the prev_amount as the new_amount for computing the next change
        prev_amount = new_amount
      
#Compute the average change:
#  new_amount from the for-loop indicates the amount of the last month
avg_change = round((new_amount-first_amount)/(total_months-1), 2)

#Set the print strings
print_strings = [
    "Financial Analysis",
    "----------------------------------",
    f"Total Months: {total_months}",
    f"Total: ${total_amount}", 
    f"Average change: ${avg_change}",
    f"Greatest Increase in Profits: {gi_date} (${g_increase})",
    f"Greatest Decrease in Profits: {gd_date} (${g_decrease})" ]

#Print the strings on terminal
print("\n")
for strings in print_strings:
    print(strings)

#set the output file path
outfilepath = os.path.join("Analysis", "budget_summary.txt")

with open(outfilepath, "w") as txtfile:
    for strings in print_strings:
        txtfile.write( strings+"\n" )