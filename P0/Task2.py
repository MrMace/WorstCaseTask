#Matt Mace
"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

uniqueNums = []
maxTime = 0
numWithMaxTime = ""
callsRow=[]
callsCol1=[]
callsCol2=[]
callsCol3=[]
numAndTime = {}

i = 0
for callsRow in calls:
    callsCol1=callsCol1+(callsRow[0].split(","))
    callsCol2=callsCol2+(callsRow[1].split(","))
    callsCol3=callsCol3+(callsRow[3].split(","))
    
    if callsCol1[i] in numAndTime:
        
        if not isinstance(numAndTime[callsCol1[i]], list):
            
            numAndTime[callsCol1[i]] = [numAndTime[callsCol1[i]]]
            
        numAndTime[callsCol1[i]].append(int(callsCol3[i]))
        numAndTime[callsCol1[i]] = sum(numAndTime[callsCol1[i]])
                
    else:
        
        numAndTime[callsCol1[i]] = int(callsCol3[i])
        
    i += 1
     
uniqueNums=(callsCol1 + callsCol2)
uniqueNumTotal = len(uniqueNums)
numWithMaxTime = max(numAndTime, key=lambda k: numAndTime[k])
maxTime = numAndTime.get(numWithMaxTime)





print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(numWithMaxTime,maxTime))
