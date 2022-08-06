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
caller_set = set()
receiver_call_set = set()
sender_text_set = set()
receiver_text_set = set()

if len(calls) > 0:
    for caller, receiver, time, duration in calls:
        caller_set.add(caller)
        receiver_call_set.add(receiver)

    for text_initiator, text_receiver, time in texts:
        sender_text_set.add(text_initiator)
        receiver_text_set.add(text_receiver)

final_set = caller_set.difference(receiver_call_set)
final_set = final_set.difference(sender_text_set)
final_set = final_set.difference(receiver_text_set)

if len(final_set) > 0:
    print("These numbers could be telemarketers: ")
    lst_final_set = list(final_set)
    lst_final_set.sort()
    for item in lst_final_set:
        print(item, sep="\n")