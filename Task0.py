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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


'''Implementation - First Record of Texts'''
if len(texts) > 0:
    first_record_of_texts = texts[0]

    if len(first_record_of_texts) == 3:
        incoming_number, answering_number, date_and_time = first_record_of_texts[0], first_record_of_texts[1], first_record_of_texts[2]
        if len(date_and_time) > 0 and ' ' in date_and_time:
            time = date_and_time.split()[1]
            print("First record of texts, {} texts {} at time {}".format(incoming_number, answering_number, time))


'''Implementation - Last Record of Calls'''
if len(calls) > 0:
    last_record_of_calls = calls[-1]


    if len(last_record_of_calls) == 4:
        incoming_number, answering_number, date_and_time, seconds = last_record_of_calls[0], last_record_of_calls[1], \
                                                           last_record_of_calls[2], last_record_of_calls[3]
        if len(date_and_time) > 0 and ' ' in date_and_time:
            time = date_and_time.split()[1]
            print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(incoming_number,
                                                            answering_number, time, seconds))

