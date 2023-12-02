
class Categories:
    
    def __init__(self):
        self._categories = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway']], 'income', ['salary', 'bonus']]


    def view(self):
        def view(l=self._categories, depth=0):
            for item in l:
                if(type(item) == str):
                    print("  "*depth, '-', item)
                else:
                    view(item, depth+1)
        view()

    def is_valid(self):
        return True

    def find_catagories(self, name):
        def find_catagories_gen()