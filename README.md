# Election_Audit
Performing analysis on Election data for Module 3 challenge.

## Overview of Election Audit
Tom, a Colorado Board of Elections employee, has requested an audit of a recent local congressional election. The following tasks were assigned to complete this audit: 

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

The raw data was provided in a CSV file consisting of a list of ballot IDs, the county each vote took place in, and the name of the candidate for who the vote was cast. Using Python, we were able to read and extract the raw data to obtain background on the results of the election. 

### Resources
* Data Source: election_results.csv
* Software: Python 3.10.2, Visual Studio Code, 1.66.2

## Election Audit Results

The results of the election audit analysis can be found below.

### I.  Total Number of Votes Cast in the Congretional Election
The total number of votes cast in this congretional election were 369,111. This value was determined by looping through each row in the csv file and adding 1 to the total count.

``` # For each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
```
### II.  Breakdown of County Results

The following 3 counties were a part of the congretional audit. 

| County | Number of Votes | Percentage of Votes |
| ------ | --------------- | ------------------- |
Denver | 306,055 | 82.8% |
Jefferson | 38,855 | 10.5% |
Arapahoe | 24,801 | 6.7% |

The county with the largest number of votes was Denver with a total of 306,055 votes, making up 82.8% of total votes.

### III.  Breakdown of Candidate Results

The following 3 candidates were a part of the congretional audit.

| Candidate | Number of Votes | Percentage of Votes |
| ------ | --------------- | ------------------- |
Diana DeGette | 272,892 | 73.8% |
Charles Casper Stockholm | 85,213 | 23.0% |
Raymon Anthony Doane | 11,606 | 3.1% |

The winning candidate with the highest number of votes was Diana Degette. She received a total of 272,892 votes, making up 73.8% of total votes. The runner up was Charles Casper Stockholm with a total of 85,213 votes, making up for 23% of votes. And finally, Raymon Anthony Doane received the least number of votes, totaling 11,606 votes which made up only 3.1%. 


## Election Audit Summary

The following Python script can be used - with some modifications - for any election. 

For example, the script can be adjusted to include analysis for larger elections nationwide. Each state can be analyzed in addition to counties within that state. This can be done by:
* declaring new variables for each state
* introducing a new for-loop to calculate the total number of votes and percentages 
* introducing a new if-statement to extract the state with the largest number of votes
* adding a new print statement to display the results

The script can also be modified to compare the number of voters in each county / state to its respective total population. This would provide insight into how many people in each county / state actually voted. This can be done by:
* adding the total population of each county / state into either the raw data file or into the script
* declaring the total populations as variables
* introducing a new for-loop to calculate the percentage of voters with respect to total population
* adding a new print statement to display the results
