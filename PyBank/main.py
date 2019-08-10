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
    #set variables to zero and create empty lists
    months_total = 0 
    total_profit = 0
    first_row = next(csvreader)
    previous_change = float(first_row[1])
    net_change_list = []
    month_list = []
    greatest_inc = []
    greatest_dec = []
    #loop through the data
    for row in csvreader:
        #count of first row
        months_total = months_total + 1
        #sum of second row, needs to be cast to a float
        total_profit = total_profit + float(row[1])   
        #total_avg = total_profit / months_total
        #finding avg. change of profit
        net_change = float(row[1]) - previous_change
        previous_change = float(row[1])
        net_change_list = net_change_list + [net_change]
        month_list = month_list + [row[0]]
        
        #finding greatest increase and decrease
        greatest_inc = max(net_change_list)
        greatest_dec = min(net_change_list)
       
        
    avg_change = sum(net_change_list) / len(net_change_list)
    
    print(months_total)
    print(total_profit)
    print(round(avg_change,2))
    print(int(greatest_inc))
    print(int(greatest_dec))
