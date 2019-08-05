import os
import csv

bank_csv = os.path.join('..','PyBank','Resources','budget_data.csv')




with open(bank_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    #to print header
        ##print(header)
    #to print all rows without header
        ##for row in csvreader:
            ##print(row)
            
