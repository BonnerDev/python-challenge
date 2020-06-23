import os
import csv

csvpath = os.path.join('..','resources','PyBank_resources.csv')
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    total = 0
    count = 0
#total number of months included in dataset
    #from the date column we need to count the number of rows there are (only one row per month)
        #date = (int(csvreader[0]))
    for row in csvreader:
        total = int(row[0]) + total
        count = int(row[0])+1
    print(count)
#net total amount of "profit/losses" over the entire period
            #profitloss = int(row[1])+ profitloss
#we need to read each row of the profit/losses column and add them altogether


#average of the changes in "profit/Losses" over the entire period
    #calcuate the average which is sum / count of how many data rows there are 
#average = total_P/L/list.count(total_P/L)
#print(average)

#print the header line 
    #csv_header = next(csvfile)
    #print(f"Header:{csv_header}")


#print financial analysis and the dotted line underneath 
#print("Financial Analysis")
#print("--------------------------------------------")
#print total months and total profit loss
#print(f"Total Months: "{datetotal}")
#print(f"Total Profit and Loss:, "sum(profitloss)")

#the greatest increase in profits (date and amount) over entire period
    #find which date has the greatest increase in profits and output this as a date format 

#the greatest decrease in losses (date and amount) over the entire period 

#script then needs to print the analysis to terminal and export a text file