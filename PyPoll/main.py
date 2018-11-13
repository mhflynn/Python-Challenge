'''Process set of poll data from file './Resources/election_data.csv.
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

if os.path.exists('./Resources/election_data.csv') :            # Confirm input file exists

    with open('./Resources/election_data.csv') as infile :      # Open the input file
        csvreader = csv.DictReader((infile))                    # Open dictionary reader for the input file

        candidateDict = {}                                      # Capture Candidate votes in a dictionary

        for row in csvreader :                                  # For each line in the input file
            if row['Candidate'] in candidateDict :              # Check for new Candidate name
                candidateDict[row['Candidate']] += 1            # Candidate name not new, increment vote count
            else :
                candidateDict[row['Candidate']] = 1             # New Candidate name, initialize vote count

        if candidateDict == {} :                                # Check if input file was empty
            print ('\nNo data found in file')                   # Empty input file, print status message

        else :                                                  # Input file was not empty
            totalvotes = sum(candidateDict.values())            # Calculate total number of votes cast
            winnercnt = 0                                       # Intialize vote count for the winner

            print ('\nElection Results')                        # Output results to the terminal
            print ('-----------------------------')
            print (f'Total vote count : {totalvotes}')
            print ('-----------------------------')

            for (candidate, votecnt) in candidateDict.items() : # For each Candidate in the election

                if votecnt > winnercnt :                        # Check if Candidate has most votes
                    winnercnt = votecnt                         # Update the winning vote count
                    winner = candidate                          # Capture name of winning candidate

                print (f'{(candidate + " "*10)[:10]} \t: '      # Output candidate name, vote percentage and count
                       f'{(100*votecnt)//totalvotes}% \t : '
                       f'{votecnt} votes')

            print ('-----------------------------')             # Output winning candidate name
            print (f'Winner : {winner} !!')
            print ('-----------------------------')

else :
    print ('\n File not found')
