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

numbers = []

for call in calls: 
    number = call[0]

    is_telemarketer = True

    for text in texts:
        if text[0] == number: 
            is_telemarketer = False
        if text[1] == number: 
            is_telemarketer = False
    for call in calls:
        if call[1] == number:
            is_telemarketer = False

    if is_telemarketer: 
        numbers.append(number)

numbers = list(set(numbers))
numbers.sort()

print("These numbers could be telemarketers: ")
for number in numbers: 
    print(number)
