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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


callsCol1 = [] 
callsCol2 = []
textCol1 = []
textCol2 = []
textCount = 0
callsCount = 0
possibleTelemarketers = []

for callsRow in calls:
    callsCol1=callsCol1+(callsRow[0].split(","))
    callsCol2=callsCol2+(callsRow[1].split(","))
       
for textRow in texts:
    textCol1 = textCol1+(textRow[0].split(","))
    textCol2 = textCol2+(textRow[1].split(","))
    
    
for call in callsCol1:
        if call not in callsCol2 and call not in textCol1 and all not in textCol2:
            possibleTelemarketers.append(call)
        
def lexo(codeType,code):    
    print(codeType)
    print()
    words = code 
    if words != []:
        for i in words: 
            print( i )
    elif words == []:
        print("None!")
        
possibleTelemarketers = lexo("These numbers could be telemarketers: ", sorted(set(possibleTelemarketers)))

    
