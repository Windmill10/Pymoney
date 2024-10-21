import sys, os, commands

def init():
    init_balance = 0; records = []
    try:
        fh = open("records/record.txt", 'r')
        init_balance = int(fh.readline())

        for line in fh.readlines():

            records.append(line.strip())
        fh.close()
    except ValueError:
        sys.stderr.write("Invalid format, deleting the contents\n")
        fh = open("records/record.txt", 'w')
        fh.write("0\n")
        fh.close()
    except FileNotFoundError:
        try:
            init_balance = input("How much money do you have? ")
            if not os.path.exists("records"):
                os.mkdir("records")

        except FileNotFoundError as err:
            sys.stderr.write(err)

        try:
            with open("records/record.txt", "w") as fh:
                fh.write(f"{init_balance}\n")
        except OSError as err:
            sys.stderr.write(err)
    try:
        init_balance = int(init_balance)

    except ValueError:
        print("Invalid amount!\nBalance is set to 0")
        init_balance = 0
        with open("records/record.txt", "w") as fh:
            fh.write(f"{init_balance}\n")


    return init_balance, records

initial_balance, records = init()

while True:

    command = input('What do you want to do (add / view / delete / exit)? ')

    if command == 'add':
        records = commands.add(records)

    elif command == 'view':
        commands.view(initial_balance, records)

    elif command == 'delete':
        records = commands.delete(initial_balance, records)
        
    elif command == 'exit':
        commands.save(initial_balance, records)
        break
    else:
        sys.stderr.write('Invalid command. Try again.\n')




