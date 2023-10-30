import config

def Add():
    print("Add some expense or income record with description and amount separated by commas: ")

    record_list = input().split(',') 

    #config.record_dict += {record.split()[0]: i.split()[1] for item in record_list}

    for record in record_list:
        item = record.split()[0]
        amount = record.split()[1]
        config.item_record.append(item)
        config.amount_record.append(amount)

    config.cur_balance = config.INITBALANCE + sum(map(int, config.amount_record))
    print(config.cur_balance)

def View(item_record, amount_record):
    if not item_record:
        print("No entries yet")
        return
    
    max_strlen = max_numlen = sum = 0

    for item, val in zip(item_record, amount_record):
        max_strlen = max(max_strlen, len(item))
        max_numlen = max(max_numlen, len(val))
    
    total_len = len("Description"+"Amount") + max_strlen  + 5 + max_numlen

    print("Description", " "*(max_strlen + 5), "Amount")
    print("="*total_len)

    for i, (item, val) in enumerate(zip(item_record, amount_record)):
        print(f"{i+1}. ", end = '')
        print(item, " "*(max_strlen + 3 - len(str(i+1))- len(item) + len("Description")) , val)

    print(f"\nNow you have {config.cur_balance} dollars")
        
def Delete():
    target = input("Item to delete: ")
    if target not in config.item_record:
        print("Item not in record")
        View(config.item_record, config.amount_record)
        return
    
    item_record = []
    amount_record = []
    index_record = []
    for (i, item), (i, val) in zip(enumerate(config.item_record), enumerate(config.amount_record)):
        if target == item: 
            item_record.append(item)
            amount_record.append(val)
            index_record.append(i)
            index = i
    if len(item_record) > 1:
          
        index = int(input("You have multiple entries of this item, which of the following would you like to delete: "))
        View(item_record, amount_record)

        while index not in index_record:    
            print(index_record)
            index = int(input("Enter a valid index: ")) - 1
    else:
        config.item_record.pop(index)
        config.amount_record.pop(index)

    config.cur_balance = config.INITBALANCE + sum(map(int, config.amount_record))
    print(config.cur_balance)
        
            