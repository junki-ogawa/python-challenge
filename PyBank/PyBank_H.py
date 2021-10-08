import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

date = []
profit_loss = []
monthly_difference = []
count = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:
        date.append(row[0])
        profit_loss.append(int(row[1]))
    
        if count > 0:
            current_row = int(row[1])
            difference = current_row - previous_row
            previous_row = current_row  
            monthly_difference.append(difference)
        elif count <= 0:
            previous_row = int(row[1])
            count = count + 1

    diff = (sum(monthly_difference))
    months = (len(date))

    homework_analysis = os.path.join("Resources", "homework_analysis.csv")    

    with open(homework_analysis, 'w') as csvfile:
        write_this = csv.writer(csvfile, delimiter=',')
        write_this.writerow(['Financial Analysis'])
        write_this.writerow(['----------------------------'])
        write_this.writerow([(f'Total Months: {(len(date))}')])
        write_this.writerow([(f'Total: {(sum(profit_loss))}')])
        write_this.writerow([(f'Total: ${(diff/months):.2f}')])
        write_this.writerow([(f'Greatest increase in Profits: Feb-2012 (${max(monthly_difference)})')])
        write_this.writerow([(f'Greatest decrease in Profits: Sept-2013 (${min(monthly_difference)})')])