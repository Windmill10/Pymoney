import commands, config

config.init()

config.INITBALANCE = int(input("How much money do you have? "))

while(True):
    command = input("What do you want to do (add / view / delete / exit)? ")

    if command == "add":
        commands.Add()
    elif command == "view":
        commands.View(config.item_record, config.amount_record)
    elif command == "delete":
        commands.Delete()
    elif command == "exit":
        break
