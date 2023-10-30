import config

def Add():
    print("Add some expense or income record with description and amount separated by commas: ")

    record_list = input().split(',') 
    print("test")

    #config.record_dict += {record.split()[0]: i.split()[1] for item in record_list}

    for record in record_list:
        item = record.split()[0]
        amount = int(record.split()[1])
        if item in config.record_dict:  #probably should make this more concise
            config.record_dict[item] += amount
        else:
            config.record_dict[item] = amount

    print(config.record_dict)
    config.cur_balance = config.INITBALANCE + sum(map(int, config.record_dict.values()))
    print(config.cur_balance)

def View():
    if not config.record_dict:
        print("No entries yet")
        return
    
    max_strlen = max_numlen = sum = 0
    for item, val in config.record_dict.items():
        max_strlen = max(max_strlen, len(item))
        max_numlen = max(max_numlen, len(str(val)))
    total_len = len("Description"+"Amount") + max_strlen  + 5 + max_numlen
    print("Description", " "*(max_strlen + 5), "Amount")
    print("="*total_len)
    for item, val in config.record_dict.items():
        print(item, " "*(max_strlen + 5 - len(item) + len("Description")) , val)
    print(f"\nNow you have {config.cur_balance} dollars")
        
def Delete():
    item = input("Item to delete: ")
    if item not in config.record_dict:
        print("Item not in record")
        View()
        return
    val = config.record_dict.pop(item)
    config.cur_balance -= val
    print(config.cur_balance)
