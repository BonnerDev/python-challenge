# Import os module 
import os 

# Import csv module 
import csv

# Set file path
budget_csv = os.path.join("Resources", "election_data.csv")

# Set a variable for the net total amount of "Profit/Losses" over the entire period
total_p_l = 0.00

# Set a variable for the total number of months included in the dataset (exclude header row)
total_months = 0

# Create empty lists to hold the profit increase, decrease and associated dates
profit = []
month = []
change = []

# Set a variable for greatest increase and decrease and associated months 
greatest_increase = 0
greatest_increase_month = ""

greatest_decrease = 0
greatest_decrease_month = ""

# Set a variable for each row total 
rowtotal = 0

# Set a variable for the first row
firstrow = 0

# Set a variable for the last row
lastrow = 0

# Set a variable for the previous row value
previousvalue = 0 


# Open and read csv file 
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Read the header row first and print to check that we have read the data correctly
    csv_header = next(csvfile)
    # print(f"Header: {csv_header}")
    
    # Read through each row of data after the header
    for row in csvreader:

        # Add profit amount to the total 
        total_p_l = (float(row[1]) + total_p_l)
       
# Print to check total profit/loss is being calculated correctly
# print(total_p_l)    

# Calculate the first and last row to determine the average change
   
        if total_months == 0:
            firstrow = (float(row[1]))

        else: 
            lastrow = (float(row[1])) 

# Pring the first and last row        
# print (firstrow)
# print (lastrow)

        # Add total months 
        total_months = (total_months+1)

# Print to check total months is being calculated correctly
# print(total_months)
        
    # Find greatest increase or decrease in profits (amount) over the entire period
        profit.append(float(row[1]))

        change.append(float(row[1]) - previousvalue)
    
        previousvalue = (float(row[1]))

# Find greatest increase or decrease in profits (month) over the entire period

        month.append(str(row[0]))

# Assign values for max and min profit variables

        max_profit = (max(profit))
        min_profit = (min(profit))

# Assign values for greatest increase and decrease variables
        greatest_increase = (max(change))
        greatest_decrease = (min(change))

# Find date of greatest increase in profits
        if float(row[1]) == (max(profit)):
                greatest_increase_month = (row[0])

# Print max profit month to check date is correct
# print(greatest_increase_month)

# Find date of greatest decrease in progits
        if float(row[1]) == (min(profit)):
                greatest_decrease_month =  (row[0])

# Print max profit month to check date is correct
# print(greatest_decrease_month)

# Calculate the average of the changes in "Profit/Losses" over the entire period
average_change = (firstrow - lastrow)/(1-total_months)

# Print to check average change is being calculated correctly
# print(average_change)


# # Print the analysis to the terminal

# Print Header
print("Financial Analysis")
print("----------------------------")

# Print total number of months
print(f"Total Months: {total_months} months")

# Print net total profit/loss  
print(f"Total: ${total_p_l:.0f}")

# Print average change in profit/loss
print(f"Average Change: ${average_change:.2f}")

# Print Greatest Profit Increase and Corresponding Date 
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase:.2f})")

# Print Greatest Profit Decrease and Corresponding Date
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease:.2f})")

# Export a text file with the results
# Specify the file to write to
output_path = os.path.join("Analysis", "Financial_Analysis.csv")

# Open the file using "write mode."
with open(output_path, 'w', newline="") as csvfile:

        # Initialise csv.writer
        csvwriter = csv.writer(csvfile, delimiter=",")

        # Write the first row
        csvwriter.writerow(["Financial Analysis"])

        # Write rows 2 to 7
        csvwriter.writerow(["----------------------------"])
        csvwriter.writerow([f"Total Months: {total_months} months"])
        csvwriter.writerow([f"Total: ${total_p_l:.0f}"])
        csvwriter.writerow([f"Average Change: ${average_change:.2f}"])
        csvwriter.writerow([f"Greatest Increase in Profits: {greatest_increase_month} (${(greatest_increase):.2f})"])
        csvwriter.writerow([f"Greatest Decrease in Profits: {greatest_decrease_month} (${(greatest_decrease):.2f})"])
