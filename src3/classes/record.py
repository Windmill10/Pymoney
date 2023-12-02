class Record:
    def __init__(self, category, description, amount):
        self._category = category
        self._description = description
        self._amount = amount

    def __repr__(self) -> str:
        return f"Record({self._category}, {self._description}, {self._amount})"
    
    
    def display(self):
        return f"{self._category}, {self._description}, {self._amount}"

    @property
    def category(self):
        return self._category
    @property
    def description(self):
        return self._description
    @property  
    def amount(self):
        return self._amount
