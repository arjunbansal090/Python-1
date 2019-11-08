''' Hacker Rank Problem Solving - 'Day of the Programmer'


Complete the dayOfProgrammer function  below. It should return a string representing the date of the 256th day of the year given.

dayOfProgrammer has the following parameter(s):

year: an integer

Input Format

A single integer denoting year y.

Constraints

1700<=y<=2700

Output Format

Print the full date of Day of the Programmer during year y in the format dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit month, and yyyy is y.

Sample Input 0

2017

Sample Output 0

13.09.2017

Sample Input 1

2016

Sample Output 1

12.09.2016

Sample Input 2

1800

Sample Output 2

12.09.1800
'''


import math
import os
import random
import re
import sys

def dayOfProgrammer(year):
    if (year == 1918):
        return '26.09.1918'
    elif ((year <= 1917) & (year%4 == 0)) or ((year > 1918) & (year%400 == 0 or ((year%4 == 0) & (year%100 != 0)))):
        return '12.09.%s' %year
    else:
        return '13.09.%s' %year

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(raw_input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

