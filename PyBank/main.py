import os
import csv

bank_csv = os.path.join('..','PyBank','Resources','budget_data.csv')

with open(bank_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
#to print header
    #print(header)
#to print all rows
    ##for row in csvreader:
        ##print(row)
#to print first row
    ##for row in csvreader:
        ##print(row[0])
    #to find the first two, set both variables to zero
    months_total = 0 
    total_profit = 0
    #loop through the data
    for row in csvreader:
        #sum of second row, needs to be cast to a float
        total_profit = total_profit + float(row[1])   
        #count of first row
        months_total = months_total + 1
    print(months_total)
    print(total_profit)
