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

'''External Reference taken - https://www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/'''

dict_calls = {}

if len(calls) > 0:
    for caller, receiver, time, duration in calls:
        if caller not in dict_calls:
            dict_calls[caller] = int(duration)
        else:
            dict_calls[caller] += int(duration)

        if receiver not in dict_calls:
            dict_calls[receiver] = int(duration)
        else:
            dict_calls[receiver] += int(duration)

if len(dict_calls) > 0:
    Valuemax, Keymax = max(zip(dict_calls.values(), dict_calls.keys()))
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(Keymax, Valuemax))
