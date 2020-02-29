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

print(texts[0])
print(calls[0])

phone_numbers = []

for item in texts: 
    phone_numbers.append(item[0])
    phone_numbers.append(item[1])

for item in calls:
    phone_numbers.append(item[0])
    phone_numbers.append(item[1])

phone_numbers = set(phone_numbers)

counts = len(phone_numbers)

print("There are {} different telephone numbers in the records.".format(counts))