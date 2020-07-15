import os
import csv

#set counters to 0
row_count = 0
winnercount = 0 

#variable list
candidate_list = []
unique_candidates = []
percentage = []
vote = []

csvpath = os.path.join("..","resources","election_data.csv")
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    
    #print the header line 
    Header = next(csvreader)
    #print(Header)

       
#first we need to find the unique candidates in the list  
    for row in csvreader:
        #find total votes cast by counting rows in spreadsheet
        row_count = (row_count +1)
        #add candidate list data to the variable list
        candidate_list.append(row[2])
        #take everything in full list and getting the unique candidate values using a set 
    unique_candidates=set(candidate_list)
        #convert the set back to a list otherwise we can not iterate in a set 
    unique_candidates=list(unique_candidates)

#test print
#print(len(unique_candidates)) #tested an it shows the number 4

#calc total votes for each using loop through the list 
for votes in range(0,len(unique_candidates)):
    voting_list = candidate_list.count((unique_candidates[votes]))

    #test above
    #print(voting_list)

    #put the above data into the list for vote
    vote.append(voting_list)

#find percentage of the votes for each candidate
    percent = round(voting_list/row_count*100,3)

    percentage.append(percent)

    


# Calculate the winner by looping through the unique candidate list
for name in range(len(unique_candidates)):

    if winnercount < vote[name]:
        winner = unique_candidates[name]
        winnercount = vote[name]

        
print("")
print("Election Results")
print("---------------------------------")
print(f"Total Votes: {row_count}")
print("---------------------------------")
print(f"{unique_candidates[0]}: {percentage[0]}% ({vote[0]})")
print(f"{unique_candidates[1]}: {percentage[1]}% ({vote[1]})")
print(f"{unique_candidates[2]}: {percentage[2]}% ({vote[2]})")
print(f"{unique_candidates[3]}: {percentage[3]}% ({vote[3]})")
print("---------------------------------")
print(f"Winner: {winner}")
print("")

#script then needs to print the analysis to terminal and export a text file
with open('file_out.txt', mode='w') as text_file:
    print("",file=text_file)
    print("Election Results",file=text_file)
    print("---------------------------------",file=text_file)
    print(f"Total Votes: {row_count}",file=text_file)
    print("---------------------------------",file=text_file)
    print(f"{unique_candidates[0]}: {percentage[0]}% ({vote[0]})",file=text_file)
    print(f"{unique_candidates[1]}: {percentage[1]}% ({vote[1]})",file=text_file)
    print(f"{unique_candidates[2]}: {percentage[2]}% ({vote[2]})",file=text_file)
    print(f"{unique_candidates[3]}: {percentage[3]}% ({vote[3]})",file=text_file)
    print("---------------------------------",file=text_file)
    print(f"Winner: {winner}",file=text_file)
    print("",file=text_file)