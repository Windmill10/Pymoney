import os, sys

def add(records):
    print("Add some expense or income record with description and amount separated by commas: ")
    try:
        record_list = input().split(',')

        for record in record_list:
            item = record.strip().split()[0]
            try:
                amount = int(record.strip().split()[1])
            except ValueError:
                sys.stderr.write("Invalid value for money\n")
                return
            records.append(f"{item}:{amount}")
    except (IndexError, ValueError):
        print("\nInvalid format, usage: description amount, description2 amount2")
    return records

def view(init_balance, records):
    if not records:
        print("No entries yet!")
    max_strlen = max_numlen = sum = 0
    
    item_record = []; amount_record = []

    try:
        for record in records:
            item_record.append(record.split(':')[0])
            amount_record.append(record.split(':')[1])
    except TypeError:
        sys.stderr.write("No entries yet!")
        return

    for item, val in zip(item_record, amount_record):
        max_strlen = max(max_strlen, len(item))
        max_numlen = max(max_numlen, len(val))
        sum += int(val)
    
    total_len = len("Description"+"Amount") + max_strlen  + 5 + max_numlen

    print("Description", " "*(max_strlen + 5), "Amount")
    print("="*total_len)

    for i, (item, val) in enumerate(zip(item_record, amount_record)):
        print(f"{i+1}. ", end = '')
        print(item, " "*(max_strlen + 3 - len(str(i+1))- len(item) + len("Description")) , val)
    
    print(f"\nNow you have {init_balance+sum} dollars")

def delete(init_balance, records):
    target = input("Item to delete: ")
    item_records = []; amount_records = []; index_record = []; found_records = []

    try:
        for i, record in enumerate(records):
            if target == record.split(':')[0]:
                item_records.append(record.split(':')[0])
                amount_records.append(record.split(':')[1])
                index_record.append(i)
                found_records.append(record)
    except:
        sys.stderr.write("Record went wrong, saving current progress and exiting program")
        #save(init_balance, records)
    
    if not found_records:
        print("Item not in record, showing list of items: ")
        view(init_balance, records)
        return
    
    if len(item_records) > 1:
        print("You have multiple entries of this item, which of the following would you like to delete?")
        view(init_balance, found_records)
        index = int(input())
    try:
        records.remove(found_records[index-1])
    except:
        print("Invalid index! Try again")
        return
    
    print(f"{target} deleted!")
    return records

def save(initial_balance, records):
    try:
        with open("records/record.txt", 'w') as fh:
            fh.write(f"{initial_balance}\n")
            for record in records:
                fh.writelines(f"{record}\n")
    except FileNotFoundError:
        sys.stderr.write("File not found")