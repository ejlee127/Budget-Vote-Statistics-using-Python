
"""
<Analyzing the election records>

Resource: election_data.csv
  with the columns 'Voter ID', 'County' and 'Candidate'.

Task: Print the followings to the terminal and a txt file.  
  * The total number of votes cast
  * A complete list of candidates who received votes
  * The percentage of votes each candidate won
  * The total number of votes each candidate won
  * The winner of the election based on popular vote.

"""
import os
import csv

#Input file
csvfilepath = os.path.join("Resources", "election_data.csv")

#Output file
outfilepath = os.path.join("Analysis", "election_analysis.txt")

#Update the result dictionaly with ky(key) and vl(value)
def result_update(result, ky, vl):
  if ky in result.keys():
    result[ky].append(vl)
  else:
    result[ky] = [vl]
  return result

#Initialize
total_votes = 0
election = {}

#Open csv file
with open(csvfilepath) as csvfile:
    election_data = csv.reader(csvfile, delimiter=',')
    header = next(election_data)
   
    for row in election_data:
      
      #Update the total number of votes
      total_votes += 1
      
      #Read the voter id and Candidate name
      voter = row[0]
      candidate = row[2]
      
      #Update the election dictionary with the new row
      election = result_update(election, candidate, voter)
      
#The analysis dictionary:
#  key stands for 'Candidate' 
#  value stores the number of votes
analysis = {ky : len(vl) for ky,vl in election.items()}

#Sort analysis according to the number of votes (by values)
sort_analysis = sorted(analysis.items(), key=lambda v:v[1], reverse=True)

#To print the results, set the print strings
print_strings = [
  f"===============================",
  f" Election Results",
  f"-------------------------------",
  f" Total Votes: {total_votes}",
  f"-------------------------------",
]

for candidate, votes in sort_analysis:
  #The percentage of votes that 'Candidate' won
  percentage = float(votes/total_votes)*100
  
  #For the aligned print, set the space after 'Candidate'
  sp = ' '*(10 - len(candidate))
  
  #Append the string for printing Candidate and percentage
  print_strings.append(
    f" {candidate.title()}:{sp} {percentage:5.2f}%  ({votes})")

#Append the strings for 'Winner' and closing lines
print_strings.append(f"-------------------------------")
print_strings.append(f" Winner: {sort_analysis[0][0]}")
print_strings.append(f"===============================")

#Print the result strings on the terminal
for string in print_strings:
  print(string)

#Print the result strings in the output file
with open(outfilepath, "w") as txtfile:
    for strings in print_strings:
        txtfile.write( strings+"\n" )