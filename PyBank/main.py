'''This Python script analyzes the records in file : "./budget_data.csv" to calculate the following:
  * The total number of months included in the data set
  * The total net amount of "Profit/Losses" over the entire period
  * The average change in "Profit/Losses" between months over the entire period
  * The greatest increase in profits (date and amount) over the entire period
  * The greatest decrease in losses (date and amount) over the entire period
'''
import csv
import os

inputfile   = 'budget_data.csv'
summaryfile = 'analysis_summary.txt'

if os.path.exists(inputfile) :                         # Confirm input file exists

    with open(inputfile) as infile :                   # Open input file
        csvreader = csv.DictReader(infile)             # Create csv reader for the input

        row = next(csvreader, None)                    # Read the first data row

        if row is not None :                           # Check for empty data input
            colDate = 'Date'                           # Key for first input column
            colPL = 'Profit/Losses'                    # Key for second input column

            monthcnt = 1                               # Input is not empty, at least 1 row
            netpl = int(row[colPL])                    # Initial net profit/loss
            maxpl = netpl                              # Initial max profit/loss
            minpl = netpl                              # Initial min profit/loss
            maxmonth = row[colDate]                    # Month for initial max profit
            minmonth = maxmonth                        # Month for initial min profit

            for row in csvreader :                     # For each remaining row of input
                monthcnt += 1                          # Increment the row count by 1
                rowpl = int(row[colPL])                # Get profit/loss for current month
                netpl += rowpl                         # Accumulate net profit/loss
                                                       
                if maxpl < rowpl :                     # Check for new max profit/loss
                    maxpl = rowpl                      # New max found, save the value
                    maxmonth = row[colDate]            # New max found, save the month

                if minpl > rowpl  :                    # Check for new min profit/loss
                    minpl = rowpl                      # New min found, save the value
                    minmonth = row[colDate]            # New min found, save the month

            # Function to output formatted analysis summary
            def summary_output (summaryout = None) :
                print ('\nFinancial Analysis'                                 , file=summaryout)
                print ('-------------------------------'                      , file=summaryout)
                print (f'Total Months : {monthcnt}'                           , file=summaryout)
                print (f'Average Change : ${netpl // monthcnt}'               , file=summaryout)
                print (f'Greatest Increase in Profits : {maxmonth} (${maxpl})', file=summaryout)
                print (f'Greatest Decrease in Profits : {minmonth} (${minpl})', file=summaryout)

            summary_output()                           # Output the results to the terminal

            with open(summaryfile, 'w') as outfile :   # Output the results to the summary file
                summary_output(outfile)

        else :
            print(f'\nNo data found in input file "{inputfile}"')
else :
    print(f'\nInput file "{inputfile}" not found')




