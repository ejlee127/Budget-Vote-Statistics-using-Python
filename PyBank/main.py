"""
<Analyzing the financial record>

Resource : budget_data.csv
  with the columns `Date` and `Profit/Losses`.
  
Task : Print the followings to the terminal and a txtfile.
  * The total number of months included in the dataset
  * The net total amount of "Profit/Losses" over the entire period
  * The average of the changes in "Profit/Losses" over the entire period
  * The greatest increase in profits (date and amount) over the entire period
  * The greatest decrease in losses (date and amount) over the entire period

"""
import os
import csv

#set the input file path
csvfilepath = os.path.join("Resources", "budget_data.csv")

#set the output file path
outfilepath = os.path.join("Analysis", "budget_summary.txt")


#the greatest increase and its date
g_increase = 0
gi_date = ""
    
#the greatest decrease and its date
g_decrease = 0
gd_date = ""

#open the input file
with open(csvfilepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
 
    #Pass the header
    next(csvreader)
    
    #Read the first row
    firstrow = next(csvreader)

    #Store the first amount of Profit/Losses of the period
    first_amount = int(firstrow[1])

    #Initialize the variable 'total_months'=total number of months
    total_months = 1

    #Initialize the variable 'total_amount'=total amount of Profit/Losses
    total_amount = first_amount
    
    #Initialize the variable 'prev_amount'
    #   =the amount of the previous month as the first amount
    prev_amount = first_amount

    #For each line=row in the files
    for row in csvreader:

        # Update the variables
        date = row[0]
        new_amount = int(row[1])
        total_months += 1
        total_amount += new_amount
        change = new_amount - prev_amount
     
        #Check whether the change is the greatest changes
        if g_increase < change:
            g_increase = change
            gi_date = date

        if g_decrease > change:
            g_decrease = change
            gd_date = date
        
        #Update the prev_amount as the new_amount for computing the next change
        prev_amount = new_amount
      
#Compute the average change:
#  'new_amount' after the for-loop indicates the last amount
avg_change = (new_amount-first_amount)/(total_months-1)

#Set the print strings
print_strings = [
    "Financial Analysis",
    "----------------------------------",
    f"Total Months: {total_months}",
    f"Total: ${total_amount}", 
    f"Average Change: ${avg_change:.2f}",
    f"Greatest Increase in Profits: {gi_date} (${g_increase})",
    f"Greatest Decrease in Profits: {gd_date} (${g_decrease})" ]

#Print the results to the terminal
for strings in print_strings:
    print(strings)


#Print the results to the output file
with open(outfilepath, "w") as txtfile:
    for strings in print_strings:
        txtfile.write( strings+"\n" )