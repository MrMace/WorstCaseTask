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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
uniqueNums = []
textRow=[]
callsRow=[]
textCol1=[]
textCol2=[]
callsCol1=[]
callsCol2=[]

for textRow in texts:
    textCol1=textCol1+(textRow[0].split(","))
    textCol2=textCol2+(textRow[1].split(","))
    
for callsRow in calls:
    callsCol1=callsCol1+(callsRow[0].split(","))
    callsCol2=callsCol2+(callsRow[1].split(","))

uniqueNums=set(textCol1 + textCol2 + callsCol1 + callsCol2)
uniqueNumTotal = len(uniqueNums)


print("There are {} different telephone numbers in the records.".format(uniqueNumTotal))



