import os
import csv

#set counters to 0
totalprofit = 0
countmonth = 0
averagechange = 0
greatincprofit = 0
greatdecprofit = 0
greatincdate = ""
greatdecdate = ""
firstrow = 0
lastrow = 0
previousrowvalue = 0
profitchange = 0

csvpath = os.path.join('..','resources','budget_data.csv')
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    
    #check the header line import by print the header line 
    csv_header = next(csvfile)
    #print(f"Header:{csv_header}")
    
    
    #we need to read each row of the profit/losses column and add them altogether
    for row in csvreader:
        totalprofit = totalprofit + int(row[1]) 
        #show that we are looking at profit/loss column    
        if countmonth == 0:
            profit = int(row[1])
            previousrowvalue = profit
            #we need to find the first row and the last row in order to find the average change
            firstrow = int(row[1])
        else: 
            lastrow = int(row[1])
            #show that we are looking for the value then the difference between that and the following value and define as profitchange
            profitchange = int(row[1]) - previousrowvalue
            #reset previous row value back to profit/loss column
            previousrowvalue = int(row[1])       
            #show that if the change in profit is larger than the counter from 0 then greatest inc in profit is equal to change in profit and same for decrease
            if  profitchange > greatincprofit:
                greatincdate = (row[0])
                greatincprofit = profitchange
                
            if profitchange < greatdecprofit:
                greatdecdate = (row[0])
                greatincprofit = profitchange

                
        #we count the months from the rows +1 each time through for loop
        countmonth = countmonth +1
    #we get average from first row minus last row then divide by 1 iterating through the month counter as month couner starts at 0 from what we set the counter to start with 

averagechange =(firstrow - lastrow)/(1-countmonth)
#print financial analysis and the dotted line underneath 
print("Financial Analysis")
print("--------------------------------------------")

#print total months and total profit loss
print(f"Total Months: {countmonth}")
print(f"Total Profit and Loss: {totalprofit}")
print(f"Average change: ${averagechange:.2f}")
print(f"greatest increase profit: {greatincdate} ${greatincprofit}")
print(f"greatest decrease profit: {greatdecdate} ${greatdecprofit}")



#script then needs to print the analysis to terminal and export a text file

with open('file_out.txt', mode='w') as text_file:
    print("Financial Analysis",file=text_file)
    print("--------------------------------------------",file=text_file)
    print(f"Total Months: {countmonth}",file=text_file)
    print(f"Total Profit and Loss: {totalprofit}",file=text_file)
    print(f"Average change: ${averagechange:.2f}",file=text_file)
    print(f"greatest increase profit: {greatincdate} ${greatincprofit}",file=text_file)
    print(f"greatest decrease profit: {greatdecdate} ${greatdecprofit}",file=text_file)