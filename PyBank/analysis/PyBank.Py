import os
import csv

#set counters to 0
totalprofit = 0
countmonth = 0
averagechange = 0
greatincprofit = 0
greatdecprofit = 0
greatincdate = 0
greatdecdate = 0
firstrow = 0
lastrow = 0
profit = 0



csvpath = os.path.join('..','resources','PyBank_resources.csv')
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    
    #check the header line import by print the header line 
    csv_header = next(csvfile)
    #print(f"Header:{csv_header}")
        
    
    #we need to read each row of the profit/losses column and add them altogether
    for row in csvreader:
        profit = (row[1])
        totalprofit = totalprofit + int(row[1]) 
        greatincprofit = max(profit)
        greatdecprofit = min(profit)
        if profit < greatincprofit:
            greatincdate = (row[0])
        if profit > greatdecprofit:
            greatdecdate = (row[0])
        #we need to find the first row and the last row in order to find the average change,    
        if countmonth == 0:
            firstrow = int(row[1])
        else: 
            lastrow = int(row[1])
        #we count the months from the rows +1
        countmonth = countmonth +1
        
    #we get average from first row minus last row then divide by 1 iterating through the month counter as month couner starts at 0 from what we set the counter to start with 
averagechange =(firstrow - lastrow)/(1-countmonth)
       
 
#print financial analysis and the dotted line underneath 
print("Financial Analysis")
print("--------------------------------------------")

#print total months and total profit loss
print(f"Total Months: {countmonth}")
print(f"Total Profit and Loss: {totalprofit}")
print(f"Average change: ${averagechange}")
print([f"greatest increase profit: {greatincdate} ${greatincprofit}"])
print([f"greatest decrease profit: {greatdecdate} ${greatdecprofit}"]) 

#the greatest decrease in losses (date and amount) over the entire period 

#script then needs to print the analysis to terminal and export a text file