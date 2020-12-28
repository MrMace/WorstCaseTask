#Matt Mace
"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

callsRow=[] 
callsCol1=[] 
callsCol2=[] 
callsCol3=[] 

localCallsCount = 0
fixedNumList = [] 
fixedCodes = [] 
mobileNumList = [] 
mobileCodes = []
telemarketersList = [] 
telemarketerCodes = [] 
unknownList = [] # catchs numbers that don't belong "should be empty"


for callsRow in calls:
    callsCol1=callsCol1+(callsRow[0].split(","))
    callsCol2=callsCol2+(callsRow[1].split(","))
    callsCol3=callsCol3+(callsRow[3].split(","))
    
    if callsRow[0].startswith("(080)"):
        if  "(" in callsRow[1] and ")" in callsRow[1]:
            fixedNumList.append(callsRow[1])
        elif " " in callsRow[1]:
            mobileNumList.append(callsRow[1]) 
        elif callsRow[1].startswith("140"):
            telemarketersList.append(callsRow[1])
        else:
            unknownList.append(callsRow[1])
  
for num in fixedNumList:
    fixedCodes.append(num[num.find("(")+1:num.find(")")])
    if num.find("(080)"):
        localCallsCount = localCallsCount + 1
    
for num in mobileNumList:
    mobileCodes.append(num[0:4])

def lexo(codeType,code):    
    print()
    print(codeType)
    words = code 
    if words != []:
        for i in words: 
            print( i )
    elif words == []:
        print("None!")

def localPercentage(local,total):
    quotient = local / total
    percentage = quotient * 100 / 1
    return percentage

print("The numbers called by people in Bangalore have codes:")
fixedCodes = lexo("Fixed Codes:",sorted(set(fixedCodes)))
mobileCodes = lexo("Mobile Codes:",sorted(set(mobileCodes)))
telemarketerCodes = lexo("Telemarketer Codes", sorted(set(telemarketerCodes)))
print()
print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(localPercentage(localCallsCount,len(fixedNumList))))
