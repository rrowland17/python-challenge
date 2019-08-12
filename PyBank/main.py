import os
import csv

bank_csv = os.path.join('Resources','budget_data.csv')

with open(bank_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    #set variables to zero and create empty lists
    months_total = 0 
    total_profit = 0
    net_change = 0
    previous_change = 0
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
        #finding avg. change of profit
        #if statement to skip the first month
        if months_total > 1:
            net_change = float(row[1]) - previous_change
            net_change_list = net_change_list + [net_change]
            
            #finding greatest increase and decrease
            greatest_inc = max(net_change_list)
            greatest_inc_month = net_change_list.index(max(net_change_list))+1

            greatest_dec = min(net_change_list)
            greatest_dec_month = net_change_list.index(min(net_change_list))+1

        previous_change = float(row[1])
        month_list = month_list + [row[0]]

    
    avg_change = sum(net_change_list) / (len(net_change_list))
    

print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {months_total}")
print(f"Total: ${total_profit:.0f}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {month_list[greatest_inc_month]} (${(str(greatest_inc))})")
print(f"Greatest Decrease in Profits: {month_list[greatest_dec_month]} (${(str(greatest_dec))})")

output = output.text
with open (output,"w") as new:
    new.write("Financial Analysis")
    new.write("\n")
    new.write("-------------------------------")  
    new.write("\n")
    new.write(f"Total Months: {months_total}")  
    new.write("\n")
    new.write(f"Total: ${total_profit:.0f}")
    new.write("\n")
    new.write(f"Average Change: ${avg_change:.2f}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {month_list[greatest_inc_month]} (${(str(greatest_inc))})")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {month_list[greatest_dec_month]} (${(str(greatest_dec))})")   
