'''Process set of poll data from file "./election_data.csv".
The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`.
Processing analyzes the votes and calculates each of the following:
  * The total number of votes cast
  * A complete list of candidates who received votes
  * The percentage of votes each candidate won
  * The total number of votes each candidate won
  * The winner of the election based on popular vote.
'''

import csv
import os

inputfile   = 'election_data.csv'
resultsfile = 'election_results.txt'

if os.path.exists(inputfile) :                                   # Confirm input file exists

    with open(inputfile) as infile :                             # Open the input file
        csvreader = csv.DictReader(infile)                       # Open dictionary reader for the input file

        candidateDict = {}                                       # Capture Candidate votes in a dictionary

        for row in csvreader :                                   # For each line in the input file
            if row['Candidate'] in candidateDict :               # Check for new Candidate name
                candidateDict[row['Candidate']] += 1             # Candidate name not new, increment vote count
            else :
                candidateDict[row['Candidate']] = 1              # New Candidate name, initialize vote count

        if candidateDict == {} :                                 # Check if input file was empty
            print (f'\nNo data found in file "{inputfile}"')     # Empty input file, print status message

        else :                                                   # Input file was not empty
            totalvotes = sum(candidateDict.values())             # Calculate total number of votes cast
            winnercnt = 0                                        # Intialize vote count for the winner
            for (candidate, votecnt) in candidateDict.items() :  # For each Candidate in the election
                if votecnt > winnercnt :                         # Check if Candidate has most votes
                    winnercnt = votecnt                          # If yes, update the winning vote count
                    winner = candidate                           # If yes, capture name of winning candidate

            # Function to output formatted election results
            def summary_output (summaryfile = None) :
                print ('\nElection Results'              , file=summaryfile)   # Output summary header
                print ('-----------------------------'   , file=summaryfile)
                print (f'Total vote count : {totalvotes}', file=summaryfile)
                print ('-----------------------------'   , file=summaryfile)

                for (candidate, votecnt) in candidateDict.items() :            # For each Candidate in the election
                    print (f'{(candidate + " "*10)[:10]}  \t: '                # Output candidate name, vote % and count
                           f'{(100*votecnt)//totalvotes}% \t: '      
                           f'{votecnt} votes'         , file=summaryfile)

                print ('-----------------------------', file=summaryfile)      # Output winning candidate name
                print (f'Winner : {winner} !!'        , file=summaryfile)
                print ('-----------------------------', file=summaryfile)

            summary_output()                                     # Output summary to the terminal

            with open(resultsfile, 'w') as outfile :
                summary_output(outfile)                          # Output summary to results file

else :
    print (f'\n File "{inputfile}" not found')
