#!/usr/bin/env python3
import sys;

print("How much money do you have?")
balance = int(input())
print("Add an expense or income record with description and amount")
record = input()

parsed_record = record.split()

if len(parsed_record) != 2:
    sys.stderr.write("Usage: Description Cash_flow")
    sys.exit(1)
    
cash_flow = int(parsed_record[1])

print(f"Now you have {balance+cash_flow} dollars.")


