import os
import csv

#set counters to 0
row_count = 0

#variable list
candidate_list = []
unique_candidates = []
#percentage = []
#vote = []

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
#print(unique_candidates[2])
#print(row_count)

        
    print("Election Results")
    print("---------------------------------")
    print(f"Total Votes: {row_count}")
    print("---------------------------------")
    

    