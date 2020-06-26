import os
import csv

#set counters to 0
totalvote = 0



csvpath = os.path.join('..','Resources','PyPoll_Resources_data.csv')
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    
    #print the header line 
    Header = next(csvreader)
    print(Header)

    #row_count = sum(1 for row in csvreader)

    candidate_list = []

    for row in csvreader:
        candidate_list.append(row[2])
    candidates=set(candidate_list)
        
    
    print("Election Results")
    print("---------------------------------")
    print()
    print(len(candidates))
    print(candidates)
    
    ##for row in csvreader:
        #candidate.add(row[2])
    #print (candidate)
    #myset = set(candidate_list)