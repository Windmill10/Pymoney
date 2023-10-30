import commands, config

config.init()

config.INITBALANCE = int(input("How much money do you have? "))

while(True):
    command = input("What do you want to do (add / view / delete / exit)? ")

    if command == "add":
        commands.Add()
    elif command == "view":
        commands.View()
    elif command == "delete":
        commands.Delete()
    elif command == "exit":
        break
