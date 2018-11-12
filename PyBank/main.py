'''This Python script analyzes the records in file : "./Resources/budget_data.csv" to calculate the following:
  * The total number of months included in the data set
  * The total net amount of "Profit/Losses" over the entire period
  * The average change in "Profit/Losses" between months over the entire period
  * The greatest increase in profits (date and amount) over the entire period
  * The greatest decrease in losses (date and amount) over the entire period
'''
import csv
import os

if os.path.exists('./Resources/budget_data.csv') :

    with open('./Resources/budget_data.csv') as infile :
        csvreader = csv.reader((infile))

        row = next(csvreader)               # Read the header row
        row = next(csvreader, None)         # Read the first row

        if row != None :                    # Check for empty data input
            monthcnt = 1                    # Input is not empty, at least 1 row
            netpl = int(row[1])             # Initial net profit/loss
            maxpl = netpl                   # Initial max profit/loss
            minpl = netpl                   # Initial min profit/loss
            maxmonth = row[0]               # Month for initial max profit
            minmonth = maxmonth             # Month for initial min profit

            for row in csvreader :          # For each remaining row of input
                monthcnt += 1               # Increment the row count by 1
                rowpl = int(row[1])         # Get profit/loss for current month
                netpl += rowpl              # Accumulate net profit/loss

                if maxpl < rowpl :          # Check for new max profit/loss
                    maxpl = rowpl           # New max found, save the value
                    maxmonth = row[0]       # New max found, save the month

                if minpl > rowpl  :         # Check for new min profit/loss
                    minpl = rowpl           # New min found, save the value
                    minmonth = row[0]       # New min found, save the month

            # Output the results to the console
            print ('\nFinancial Analysis')
            print ('-------------------------------')
            print (f'Total Months : {monthcnt}')
            print (f'Average Change : ${netpl // monthcnt}')
            print (f'Greatest Increase in Profits : {maxmonth} (${maxpl})')
            print (f'Greatest decrease in profits : {minmonth} (${minpl})')

            #Output the results to file analysis_summary.txt
            with open('./Resources/analysis_summary.txt', 'w') as outfile :
                print ('\nFinancial Analysis', file=outfile)
                print ('-------------------------------', file=outfile)
                print (f'Total Months : {monthcnt}', file=outfile)
                print (f'Average Change : ${netpl // monthcnt}', file=outfile)
                print (f'Greatest Increase in Profits : {maxmonth} (${maxpl})', file=outfile)
                print (f'Greatest decrease in profits : {minmonth} (${minpl})', file=outfile)

        else :
            print('\nNo data found in input file {"./Resources/budget_data.csv"}')
else :
    print(f'\nInput file "{"./Resources/budget_data.csv"}" not found')




