import sys, os
from classes import categories as cat
from classes import record as rec

class Records:
    
    def _is_empty(self):
        if len(self._records) == 0:
            sys.stderr.write("No entries yet!")
            return True
        return False
    
    def _read_and_write(self):
        try:
            with open("user_records/record.txt", 'r') as fh:
                self._init_balance = int(fh.readline())
                for line in fh.readlines():
                    cate, desc, amt = line.strip().split(':')
                    self._records.append(rec.Record(cate, desc, amt))
        except ValueError:
            try:
                self._init_balance = int(input("How much money do you have? "))
                with open("user_records/record.txt", 'w') as fh:
                    fh.write(f"{self._init_balance}\n")
            except ValueError:
                sys.stderr.write("Invalid amount!\nBalance is set to 0")
                self._init_balance = 0
                with open("user_records/record.txt", "w") as fh:
                    fh.write(f"{self._init_balance}\n")

    def __init__(self):
        self._records = []
        self._init_balance = 0

        try:
            Records._read_and_write(self)
            return

        except FileNotFoundError:
            try:
                if not os.path.exists("user_records"):
                    os.mkdir("user_records")
                with open("user_records/record.txt", "w") as fh:
                    pass
            except FileNotFoundError as err:
                sys.stderr.write(err)

        Records._read_and_write(self)

    def __repr__(self) -> str:
        return f"Records({self._records})"
    
    def add(self, records): #record: category1, description1, amount1, category2, description2, amount2, ...
        l = []
        try:
            for record in records.split(','):
                cate, desc, amt = record.strip().split()
                amt = int(amt) 
                if(cat.Categories.is_valid(cat.Categories(), cate) == False):
                    sys.stderr.write("Invalid category")
                    return
                l.append(rec.Record(cate, desc, amt))

        except IndexError:
            sys.stderr.write("Invalid format, usage: category1, description1, amount1, category2, description2, amount2, ...")
        except ValueError:
            sys.stderr.write("Invalid value for money")

        self._records.extend(l)
        

    def view(self):
        if(self._is_empty()):
            return
        sum = 0
        for i, record in enumerate(self._records):
            sum += int(record.amount)
            print(f"{i+1}. {record.display()}")
        print(f"\nNow you have {self._init_balance+sum} dollars")

    def delete(self, target):
        if(self._is_empty()):
            return
        found_index = []
        for i, record in enumerate(self._records):
            if target == record.description:
                found_index.append(i)
        if len(found_index) == 1:
            del self._records[found_index[0]]
        elif len(found_index) > 1:
            for i in found_index:
                print(f"{i+1}. {self._records[i].display()}")

            while True:
                try:
                    delete_index = int(input("Which record do you want to delete? "))
                    if delete_index > len(found_index) or delete_index < 1:
                        raise ValueError
                    break
                except ValueError:
                    sys.stderr.write("Invalid index, try again")
            del self._records[found_index[delete_index-1]]
            print("Record deleted")
        else:
            sys.stderr.write("No such record")

    def find(self, target):
        if(self._is_empty()):
            return
        for i, record in enumerate(self._records):
            if record.category in target:
                print(f"{i+1}. {record.display()}")
        
    def save(self):
        try:
            with open("user_records/record.txt", 'w') as fh:
                fh.write(f"{self._init_balance}\n")
                for record in self._records:
                    fh.write(f"{record.category}:{record.description}:{record.amount}\n")
        except OSError as err:
            sys.stderr.write(err)

    
    >>> def	extractPos1(tup):
...					return	tup[1]
...
>>>	M.sort(key=extractPos1)