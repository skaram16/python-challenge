#import my dependencies
import os
import csv

#define all variables
total_months = 0
net_revenue = 0
change_monthly = []
monthly_count = []
greatest_increase = 0
greatest_decrease = 0
month_increase = 0
month_decrease = 0


#create a file path for the data
budget_data_path = os.path.join("../PyBank/Resources/budget_data.csv")


#open and read the data path
with open(budget_data_path) as budget_data_file:
    reader = csv.reader(budget_data_file, delimiter=',')

    #read the header row first
    header = next(reader)
    row = next(reader)

    #calculate total months
    previous_row = int(row[1])
    total_months = total_months + 1

    #calculate the total revenue
    net_revenue = net_revenue + int(row[1])

    #calculate the greatest increases
    greatest_increase = int(row[1])
    month_increase = row[0]

    #read each row after the headers
    for row in reader:

        #calculate the total number of months in dataset
        total_months = total_months + 1

        #calculate the total of profit/loss of whole period
        net_revenue = net_revenue + int(row[1])

        #calculate changes for months
        revenue_change = int(row[1]) - previous_row
        change_monthly.append(revenue_change)
        previous_row = int(row[1])
        monthly_count.append(row[0])

        #calculate the greatest increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            month_increase = row[0]

        #calculate the greatest decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            month_decrease = row[0]

    #calculate the mean and the date
    average_change = sum(change_monthly) / len(change_monthly)

    highest = max(change_monthly)
    lowest = min(change_monthly)

#print all values
print(f"Financial Analysis")
print(f"-------------------------")
print(f"Total Months: {total_months}")
print(f"Total Amount: ${net_revenue}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase In Profits:, {month_increase}, (${highest})")
print(f"Greatest Decrease In Profits:, {month_decrease}, (${lowest})")

#delegating what file to write edited data to
output_file = os.path.join("../PyBank/Analysis/budget_data_revised.txt")

#open the file as a text file
with open(output_file, 'w',) as txtfile:

    #write the data in new format
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_revenue}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase In Profits:, {month_increase}, (${highest})\n")
    txtfile.write(f"Greatest Decrease In Profits:, {month_decrease}, (${lowest})\n")
