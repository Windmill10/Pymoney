#!/usr/bin/env python3
import sys;

print("How much money do you have?")
balance = int(input())

print("Add some expense or income record with description and amount separated by commas: ")

record_list = input().split(',') #split input into individual description and amount

record_dict = {item.split()[0]: item.split()[1] for item in record_list} #dictionary comprehension to parse description
                                                                         #and amount into key value pairs

for item, val in record_dict.items():  #print each record
    print(item, val)

balance += sum(map(int, record_dict.values())) #add all values mapped into int

print(f"You now have {balance} dollars")




